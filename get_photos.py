import flickrapi
import json
import os

api_key = os.environ['FLICKR_KEY']
api_secret = os.environ['FLICKR_SECRET']

flickr = flickrapi.FlickrAPI(api_key, api_secret)


def get_image_by_location(lat, lon):
    """Get data for a photo with specified latitude and longitude."""

    photo = flickr.photos.search(per_page='1', format='json', lat=lat, lon=lon)

    photo_info = json.loads(photo)
    print photo_info
    return photo_info


def get_image_url(photo_info):
    """Get url for a photo, given json string returned from Flickr API."""

    photo_id = photo_info['photos']['photo'][0]['id']
    user_id = photo_info['photos']['photo'][0]['owner']

    photo_source_template = "https://www.flickr.com/photos/{}/{}/"
    photo_source_url = photo_source_template.format(user_id, photo_id)
    return photo_source_url

laguna_beach_photo_info = get_image_by_location(33.5422, -117.7831)
laguna_beach_photo_source_url = get_image_url(laguna_beach_photo_info)
print laguna_beach_photo_source_url
