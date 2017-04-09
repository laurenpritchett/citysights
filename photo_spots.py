# Helper functions to server.py

import os

from jinja2 import StrictUndefined

from flask import (Flask, session)

from model import User, Photo, UserPhoto, db

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

google_maps_api_key = os.environ['GOOGLE_KEY']


def get_user_by_email(email):
    """Get user by email."""

    user = User.query.filter(User.email == email).first()

    return user


def get_user_by_id(user_id):
    """Get user by user_id"""

    user = User.query.filter(User.user_id == user_id).first()
    return user


def get_photos_by_user(user_id):
    """Get saved photo spots by user."""

    saved_photos = UserPhoto.query.filter(UserPhoto.user_id == user_id).all()

    saved_photos_info = []

    for saved_photo in saved_photos:
        saved_photos_info.append({'photo_id': saved_photo.photo_id,
                                  'img_src': saved_photo.photo.img_src,
                                  'user_id': saved_photo.user_id
                                  })

    return saved_photos_info


def user_exists(user):
    """Check if user exists in database."""

    if user is not None:
        return True
    else:
        return False


def correct_password(user, password):
    """Check if user entered the right password."""

    if user.password == password:
        return True
    else:
        return False


def register_user(user_info):
    """Add new user to database."""

    password = user_info.get("password")
    first_name = user_info.get("fname")
    last_name = user_info.get("lname")
    email = user_info.get("email")

    new_user = User(email=email, password=password, first_name=first_name, last_name=last_name)
    db.session.add(new_user)
    db.session.commit()
    new_user = User.query.filter(User.email == email).one()

    return new_user


def save_photo_spot(img_src, photo_id, user_id):
    """Save photo to database."""

    # city_id = session['city_id']

    new_user_photo = UserPhoto(user_id=user_id, photo_id=photo_id)

    if not Photo.query.filter(Photo.photo_id == photo_id).all():
        new_photo = Photo(img_src=img_src, photo_id=photo_id)
        db.session.add(new_photo)

    db.session.add(new_user_photo)
    db.session.commit()


def is_saved(photo_id):
    """Check if photo spot has been saved by current user."""

    saved = UserPhoto.query.filter(UserPhoto.user_id == session['user_id'],
                                   UserPhoto.photo_id == photo_id).first()

    return saved


def remove_photo_spot(photo_id, user_id):
    """Remove photo from database."""

    photo = UserPhoto.query.filter(UserPhoto.photo_id == photo_id, UserPhoto.user_id == user_id).first()
    db.session.delete(photo)
    db.session.commit()
