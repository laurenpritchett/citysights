"""Google Maps Geocoding function."""

import googlemaps
import os

google_maps_api_key = os.environ['GOOGLE_KEY']

gmaps = googlemaps.Client(key=google_maps_api_key)


def get_address_by_lat_lng(lat, lng):
    """Turn lat/lng into human-readable address.

    >>> get_address_by_lat_lng(37.808480, -122.475853)
    u'Coastal Trail, San Francisco, CA 94129, USA'

    """

    reverse_geocode_result = gmaps.reverse_geocode((lat, lng))

    # Return formatted address
    # Looks like u'Coastal Trail, San Francisco, CA 94129, USA'

    return reverse_geocode_result[0]['formatted_address']

# print get_address_by_lat_lng(37.808480, -122.475853)
