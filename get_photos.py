import flickrapi
import json
import os

api_key = os.environ[u'FLICKR_KEY']
api_secret = os.environ[u'FLICKR_SECRET']

flickr = flickrapi.FlickrAPI(api_key, api_secret)


def get_photos_by_location(lat, lon):
    """Get URL for interesting photos with specified latitude and longitude."""
    photo_urls = []

    photos = flickr.photos.search(per_page='10', format='json', lat=lat, lon=lon,
                                  radius='1', sort='interestingness-desc')

    photo_info = json.loads(photos)

    for info in range(len(photo_info['photos']['photo'])):
        photo_id = photo_info['photos']['photo'][0]['id']
        user_id = photo_info['photos']['photo'][0]['owner']
        photo_source_template = "https://www.flickr.com/photos/{}/{}/"
        photo_source_url = photo_source_template.format(user_id, photo_id)

        farm_id = photo_info['photos']['photo'][0]['farm']
        server_id = photo_info['photos']['photo'][0]['server']
        photo_secret = photo_info['photos']['photo'][0]['secret']

        photo_url_template = "https://farm{}.staticflickr.com/{}/{}_{}.jpg"
        photo_url = photo_url_template.format(farm_id, server_id, photo_id, photo_secret)
        photo_urls.append([photo_source_url, photo_url])
    return photo_urls


laguna_beach_photo_urls = get_photos_by_location(33.5422, -117.7831)
print laguna_beach_photo_urls
