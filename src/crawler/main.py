from src.crawler.crawl_preview import *
from src.crawler.crawl_detail import *

def get_restaurant(html):
  restaurant_preview = {
    'name': get_restaurant_name(html),
    'image_thumb': get_restaurant_image_thumb(html),
    'price': get_restaurant_price(html),
    'type': get_restaurent_type(html),
    'awards': get_restaurant_awards(html),
    'coords': get_restaurant_coordinates(html),
    'link_to_detail_url': get_retaurent_detail_url(html)
  }

  return restaurant_preview

def get_restaurant_details(html):
  detail = {
    'address': get_detail_address(html),
    'phone': get_detail_phone_number(html),
    'website': get_detail_website(html),
    'opening_hours': get_detail_opening_hours(html),
    'description': get_detail_description(html),
    'facilities_and_services': get_detail_facilities_and_services(html)
  }

  return detail
