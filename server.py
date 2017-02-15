"""Photo Spots."""

import flickrapi

import json

import os

from get_photos import (api_key, api_secret, flickr, get_photos_by_location,
                        get_photo_location, get_photo_url)

from get_address import gmaps, get_address_by_lat_lng

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request, flash,
                   session)

from flask_debugtoolbar import DebugToolbarExtension

from model import City, connect_to_db, db

from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

google_maps_api_key = os.environ['GOOGLE_KEY']


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route('/user-login')
def user_login():
    """Render HTML template with login form."""

    return render_template("user-login.html")


@app.route('/user-login', methods=["POST"])
def handle_user_login():
    """Handles login and registration for new users."""

    email = request.form.get("email")
    password = request.form.get("password")

    # Check if user is in the database. If not, create a new user.
    try:
        current_user = User.query.filter(User.email == email).one()
    except NoResultFound:
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Welcome stranger!')
        return redirect("/")

    # Verify that user has entered the correct password.
    if current_user.password == password:
        session['user_id'] = current_user.user_id
        flash('Welcome back!')
        return redirect("/")
    else:
        flash('Incorrect email or password provided.')

    return redirect("/")


@app.route('/user-logout')
def logout():
    """Remove user_id from session and redirect to the home page."""

    del session['user_id']
    flash('See you later!')
    return redirect("/")


@app.route('/user/<user_id>')
def user_page(user_id):
    """ Show user profile."""

    current_user = User.query.filter(User.user_id == user_id).one()

    title_and_score = db.session.query(Movie.title,
                                       Rating.score).\
        join(Rating).\
        filter(Rating.user_id == user_id).\
        all()

    progress = progress_tracker(user_id)

    return render_template("user-profile.html",
                           current_user=current_user,
                           title_and_score=title_and_score,
                           progress=progress,
                           )


@app.route('/search-results')
def search_city():
    """Return photo results from city search."""

    search = request.args.get('city-search')
    city_search = '%{}%'.format(search)
    city = City.query.filter(City.name.ilike(city_search)).first()

    if city is not None:
        name = city.name
        lat = city.lat
        lng = city.lng

        url_pairs = get_photos_by_location(lat, lng)
    else:
        name = None
        url_pairs = None

    return render_template("search-results.html",
                           name=name,
                           url_pairs=url_pairs)


@app.route('/photo-details/<photo_id>')
def show_photo_and_location(photo_id):
    """Show photo and location details."""

    img_src = get_photo_url(photo_id)

    location_details = get_photo_location(photo_id)

    lat = location_details['lat']
    lng = location_details['lng']

    address = get_address_by_lat_lng(lat, lng)

    # joined_address = address.split(" ").join("")

    return render_template("photo-details.html",
                           img_src=img_src,
                           lat=lat,
                           lng=lng,
                           address=address,
                           google_maps_api_key=google_maps_api_key)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
