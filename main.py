from src.utils.logger import logger
from src.helper.request import request_to_restaurant_list_page, request_to_restaurant_details_page
from src.crawler.soup import get_list_restaurant_elements, get_restaurant_details_element
from src.crawler.main import get_restaurant, get_restaurant_details
from src.helper.file import write_data_to_json_file
from src.utils.get_current_date_str import get_current_date_str
from src.utils.get_file_path import get_michelin_star_data_file_path

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

  current_date = get_current_date_str()

  while True:
    if (START_PAGE >= END_PAGE and END_PAGE != -1):
      break
    
    logger.info('Star: {} - Crawling page: {}'.format(MICHELIN_STAR_NUM, START_PAGE))
    # Get Restaurant List
    res_restaurant_list = request_to_restaurant_list_page(MICHELIN_STAR_NUM, START_PAGE)
    if (res_restaurant_list):
      list_restaurant_elements = get_list_restaurant_elements(res_restaurant_list)
    
    if len(list_restaurant_elements) == 0:
      if MICHELIN_STAR_NUM < 3 and is_continue_crawling_next_star:
        MICHELIN_STAR_NUM += 1
        START_PAGE = 1
        END_PAGE = -1
      else:
        logger.info('✨ Done')
        break
    else:
      for item in list_restaurant_elements:
        restaurant_preview = get_restaurant(item)
        logger.info('Crawling: {}'.format(restaurant_preview['name']))
      
        # Get Restaurant Details
        res_restaurant_details = request_to_restaurant_details_page(restaurant_preview['link'])
        if res_restaurant_details:
          restaurant_details_element = get_restaurant_details_element(res_restaurant_details)
          restaurant_details = get_restaurant_details(restaurant_details_element)

          # Merge 2 dicts
          restaurant = dict(restaurant_preview, **restaurant_details)
          # Add time
          restaurant['created_at'] = current_date
          restaurant['updated_at'] = current_date
          
          RESTAURANTS.append(restaurant)

      # Store data to json file
      path = get_michelin_star_data_file_path(current_date)
      write_data_to_json_file(RESTAURANTS, path)
      
      RESTAURANTS = []
      START_PAGE += 1

main()
