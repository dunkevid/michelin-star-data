import requests

from src.constants import RESTAURANTS_URL

# 1 star: https://guide.michelin.com/at/en/restaurants/1-star-michelin/page/1
# 2 star: https://guide.michelin.com/at/en/restaurants/2-stars-michelin/page/1
# 3 star: https://guide.michelin.com/at/en/restaurants/3-stars-michelin/page/1
def _get_michelin_url(star_number, page = 1):
  star_suffix = 'star-michelin' \
    if star_number == 1 \
    else 'stars-michelin'
  
  url = '{}/{}-{}/page/{}'.format(RESTAURANTS_URL, star_number, star_suffix, page)
  
  return url

def request_to_restaurant_list_page(star_num = 1, page = 1):
  try:
    req = requests.get(_get_michelin_url(star_num, page))
    return req.text
  except Exception as ex:
    print('[ERROR] {}'.format(ex))
    return False

def request_to_restaurant_details_page(detail_url):
  try:
    req = requests.get(detail_url)
    return req.text
  except Exception as ex:
    print('[ERROR] {}'.format(ex))
    return False