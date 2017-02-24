# Helper functions to server.py

import os

from jinja2 import StrictUndefined

from flask import (Flask, request, flash,
                   session)

from model import City, User, Photo, db


app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

google_maps_api_key = os.environ['GOOGLE_KEY']


def get_user():
    """Get user by email."""

    email = request.form.get("email")
    user = User.query.filter(User.email == email).first()

    return user


def get_user_by_id(user_id):
    """Get user by user_id"""

    user = User.query.filter(User.user_id == user_id).first()
    return user


def get_photos_by_user(user_id):
    """Get saved photo spots by user."""

    saved_photos = Photo.query.filter(Photo.user_id == user_id).all()

    saved_photos_info = []

    for saved_photo in saved_photos:
        saved_photos_info.append({'photo_id': saved_photo.photo_id,
                                  'img_src': saved_photo.img_src,
                                  'city_id': saved_photo.city_id,
                                  'user_id': saved_photo.user_id
                                  })

    return saved_photos_info


def user_exists(user):
    """Check if user exists in database."""

    if user is not None:
        return True
    else:
        return False


def correct_password(user):
    """Check if user entere the right password."""

    password = request.form.get("password")

    if user.password == password:
        session['user_id'] = user.user_id
        flash('Welcome back!')
        return True
    else:
        flash('Incorrect password provided.')
        return False


def register_user():
    """Add new user to database."""

    email = request.form.get("email")
    password = request.form.get("password")
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")

    new_user = User(email=email, password=password, first_name=first_name, last_name=last_name)
    db.session.add(new_user)
    db.session.commit()
    user = User.query.filter(User.email == email).one()
    session['user_id'] = user.user_id
    flash('Welcome to Photo Spots!')
    return new_user


def log_out():
    """Remove user from session."""

    del session['user_id']
    flash('See you later!')


def get_city():
    """Get city from search."""

    search = request.args.get('city-search')
    city_search = '%{}%'.format(search)
    city = City.query.filter(City.name.ilike(city_search)).first()
    return city


def save_photo_spot():
    """Save photo to database."""

    img_src = request.form.get("src")
    photo_id = request.form.get("id")
    city_id = City.query.filter(City.name == session['city_name']).one().city_id
    user_id = session['user_id']

    new_photo = Photo(img_src=img_src, photo_id=photo_id, city_id=city_id, user_id=user_id)
    db.session.add(new_photo)
    db.session.commit()


def is_saved(photo_id):
    """Check if photo spot has been saved by current user."""

    saved = Photo.query.filter(Photo.user_id == session['user_id'],
                               Photo.photo_id == photo_id).first()

    return saved


def remove_photo_spot():
    """Remove photo from database."""

    photo_id = request.form.get("id")
    user_id = session['user_id']

    photo = Photo.query.filter(Photo.photo_id == photo_id, Photo.user_id == user_id).first()
    db.session.delete(photo)
    db.session.commit()
