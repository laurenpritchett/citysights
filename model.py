from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


################################################################################
# Model definition

class City(db.Model):
    """Cities with lat/lon information."""

    __tablename__ = "cities"

    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(33), nullable=True)
    lat = db.Column(db.Numeric, nullable=True)
    lng = db.Column(db.Numeric, nullable=True)
    country = db.Column(db.String(32), nullable=True)
    iso2 = db.Column(db.String(3), nullable=True)
    province = db.Column(db.String(43), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<City id=%s name=%s country=%s>" % (self.city_id, self.name, self.country)


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
