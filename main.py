from datetime import date

from src.request import request_to_restaurant_list_page, request_to_restaurant_details_page
from src.crawler.soup import get_list_restaurant_elements, get_restaurant_details_element
from src.crawler.main import get_restaurant, get_restaurant_details
from src.file import write_data_to_json_file
from src.utils import get_michelin_star_data_path

def main(
  star = 1,
  start_page = 1,
  end_page = -1,
  is_continue_crawling_next_star = True
):
  RESTAURANTS = []

  MICHELIN_STAR_NUM = star
  START_PAGE = start_page
  END_PAGE = end_page

  while True:
    if (START_PAGE >= END_PAGE and END_PAGE != -1):
      break
    
    print('Star: {} - Crawling page: {}'.format(MICHELIN_STAR_NUM, START_PAGE))
    # Get Restaurant List
    res_restaurant_list = request_to_restaurant_list_page(MICHELIN_STAR_NUM, START_PAGE)
    if (res_restaurant_list):
      list_restaurant_elements = get_list_restaurant_elements(res_restaurant_list)
    
    if (len(list_restaurant_elements) == 0):
      if (MICHELIN_STAR_NUM < 3 and is_continue_crawling_next_star):
        MICHELIN_STAR_NUM += 1
        START_PAGE = 1
        END_PAGE = -1
      else:
        print('✨ Done')
        break
    else:
      for item in list_restaurant_elements:
        restaurant_preview = get_restaurant(item)
        print('Crawling: {}'.format(restaurant_preview['name']))
      
        # Get Restaurant Details
        res_restaurant_details = request_to_restaurant_details_page(restaurant_preview['link_to_detail_url'])
        if (res_restaurant_details):
          restaurant_details_element = get_restaurant_details_element(res_restaurant_details)
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
      START_PAGE += 1
