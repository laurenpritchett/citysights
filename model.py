from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


################################################################################
# Model definition

class City(db.Model):
    """City with location information."""

    __tablename__ = "cities"

    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(33), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(32), nullable=False)
    iso2 = db.Column(db.String(3), nullable=False)
    province = db.Column(db.String(43), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<City id=%s name=%s country=%s>" % (self.city_id, self.name, self.country)


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


class Photo(db.Model):
    """Photo with location information."""

    __tablename__ = "photos"

    photo_id = db.Column(db.Integer, primary_key=True)
    img_src = db.Column(db.String(200), nullable=False)
    city_id = db.Column(db.Integer)


class UserPhoto(db.Model):
    """Association table for user and photo spot."""

    __tablename__ = "users_photos"

    user_photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    photo_id = db.Column(db.Integer,
                         db.ForeignKey('photos.photo_id'),
                         nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)



################################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hbproject'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
