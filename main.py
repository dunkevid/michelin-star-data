from bs4 import BeautifulSoup
from datetime import date

from src.constants import HTML_CLASS_NAME
from src.request import request_to_restaurant_list_page, request_to_restaurant_details_page
from src.crawler.main import get_restaurant, get_restaurant_details
from src.file import write_data_to_json_file
from src.utils import get_michelin_star_data_path

MICHELIN_STAR_NUM = 1
PAGE = 1
RESTAURANTS = []

while True:
  print('Star: {} - Crawling page: {}'.format(MICHELIN_STAR_NUM ,PAGE))
  # Get Restaurant List
  res_restaurant_list = request_to_restaurant_list_page(MICHELIN_STAR_NUM, PAGE)
  if (res_restaurant_list):
    soup_restaurant_list = BeautifulSoup(res_restaurant_list, 'lxml')

    list_restaurants_elements = soup_restaurant_list.find_all(
      'div',
      class_=HTML_CLASS_NAME['list_restaurants']
    )
  
  if (len(list_restaurants_elements) == 0):
    if (MICHELIN_STAR_NUM < 3):
      MICHELIN_STAR_NUM += 1
      PAGE = 1
    else:
      print('✨ Done')
      break
  else:
    for item in list_restaurants_elements:
      restaurant_preview = get_restaurant(item)
      print('Crawling: {}'.format(restaurant_preview['name']))
    
      # Get Restaurant Details
      res_restaurant_details = request_to_restaurant_details_page(restaurant_preview['link_to_detail_url'])
      soup_restaurant_details = BeautifulSoup(res_restaurant_details, 'lxml')
      restaurant_details_element = soup_restaurant_details.find(
        'div',
        class_=HTML_CLASS_NAME['d_r_details']
      )
      restaurant_details = get_restaurant_details(restaurant_details_element)

      # Merge 2 dicts
      restaurant = dict(restaurant_preview, **restaurant_details)
      # Add time
      restaurant['created_at'] = date.today().strftime("%B %d, %Y")
      restaurant['updated_at'] = date.today().strftime("%B %d, %Y")
      
      RESTAURANTS.append(restaurant)

    # Store data to json file
    path = get_michelin_star_data_path(MICHELIN_STAR_NUM)
    write_data_to_json_file(RESTAURANTS, path)
    
    RESTAURANTS = []
    PAGE += 1

