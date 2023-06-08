from src.utils.constants import RESTAURANTS_URL

# 1 star: https://guide.michelin.com/at/en/restaurants/1-star-michelin/page/1
# 2 star: https://guide.michelin.com/at/en/restaurants/2-stars-michelin/page/1
# 3 star: https://guide.michelin.com/at/en/restaurants/3-stars-michelin/page/1
def get_michelin_url(star_number, page = 1):
  star_suffix = 'star-michelin' \
    if star_number == 1 \
    else 'stars-michelin'
  
  url = '{}/{}-{}/page/{}'.format(RESTAURANTS_URL, star_number, star_suffix, page)
  
  return url
