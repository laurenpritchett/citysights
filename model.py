from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


################################################################################
# Model definition

class User(db.Model):
    """User of photo spots website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)

    @classmethod
    def by_id(cls, user_id):
        """Get user by id."""

        return cls.query.filter_by(user_id=user_id).first()


class UserPhoto(db.Model):
    """Middle table for User and Photo relationship."""

    __tablename__ = "users_photos"

    users_photos_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))
    photo_id = db.Column(db.String(200),
                         db.ForeignKey('photos.photo_id'))

    user = db.relationship("User",
                           backref=db.backref("users_photos",
                                              order_by=users_photos_id))

    photo = db.relationship("Photo",
                            backref=db.backref("users_photos",
                                               order_by=users_photos_id))


class Photo(db.Model):
    """Photo saved by a user."""

    __tablename__ = "photos"

    photo_id = db.Column(db.String(200), primary_key=True)
    img_src = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Photo photo_id=%s img_src=%s>" % (self.photo_id, self.img_src)

    @classmethod
    def by_id(cls, photo_id):
        """Get photo by id."""

        return cls.query.filter_by(photo_id=photo_id).first()

################################################################################
# Helper functions


def connect_to_db(app, db_uri=None):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgresql:///hbproject'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


def example_data():
    """Create some sample data."""
    karen = User(first_name='karen',
                 last_name='smith',
                 email='ksmith@gmail.com',
                 password='happy123')
    bob = User(first_name='bob',
               last_name='johnson',
               email='bjohnson@gmail.com',
               password='umbrella24')
    sally = User(first_name='sally',
                 last_name='smith',
                 email='ksmith@gmail.com',
                 password='happy123')

    db.session.add_all([karen, bob, sally])
    db.session.commit()


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
