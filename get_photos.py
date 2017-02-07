import flickrapi
import json
import os

api_key = os.environ[u'FLICKR_KEY']
api_secret = os.environ[u'FLICKR_SECRET']

flickr = flickrapi.FlickrAPI(api_key, api_secret)


def get_photos_by_location(lat, lon):
    """Get URL for a photo with specified latitude and longitude."""

    photo = flickr.photos.search(per_page='1', format='json', lat=lat, lon=lon)

    photo_info = json.loads(photo)

    photo_id = photo_info['photos']['photo'][0]['id']
    user_id = photo_info['photos']['photo'][0]['owner']
    photo_source_template = "https://www.flickr.com/photos/{}/{}/"
    photo_source_url = photo_source_template.format(user_id, photo_id)
    return photo_source_url

laguna_beach_photo_url = get_photos_by_location(33.5422, -117.7831)
print laguna_beach_photo_url
