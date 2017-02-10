"""Photo Locations."""

import flickrapi

import json

import os

from get_photos import (api_key, api_secret, flickr, get_photos_by_location,
                        get_photo_location, get_photo_url)

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request, flash,
                   session)

from flask_debugtoolbar import DebugToolbarExtension

from model import City, connect_to_db, db

from secret import googleMapsApiKey

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

google_maps_api_key = os.environ['GOOGLE_KEY']


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route('/search-results')
def search_city():
    """Return photo results from city search."""

    search = request.args.get('city-search')
    city_search = '%{}%'.format(search)
    city = City.query.filter(City.name.ilike(city_search)).first()
    name = city.name
    lat = city.lat
    lng = city.lng

    url_pairs = get_photos_by_location(lat, lng)

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
    neighborhood = location_details['neighborhood']
    locality = location_details['locality']
    country = location_details['country']

    return render_template("photo-details.html",
                           img_src=img_src,
                           lat=lat,
                           lng=lng,
                           neighborhood=neighborhood,
                           locality=locality,
                           country=country,
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
