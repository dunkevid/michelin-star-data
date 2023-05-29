import requests
from bs4 import BeautifulSoup

from src.constants import HTML_CLASS_NAME
from src.utils import get_michelin_url
from src.crawler.main import get_restaurant, get_restaurant_details

star_num = 3
req = requests.get(get_michelin_url(3, 100))

soup = BeautifulSoup(req.text, 'lxml')

list_restaurants_elements = soup.find_all('div', class_=HTML_CLASS_NAME['list_restaurants'])


while True:
  if (len(list_restaurants_elements) == 0):
    print('Not found')
    break
  else:
    for item in list_restaurants_elements:
      try:
        restaurant_preview = get_restaurant(item)
      
        # Get Restaurant Details
        req_detail = requests.get(restaurant_preview['link_to_detail_url'])
        detail_soup = BeautifulSoup(req_detail.text, 'lxml')
        restaurant_details_element = detail_soup.find('div', class_=HTML_CLASS_NAME['d_r_details'])
        restaurant_details = get_restaurant_details(restaurant_details_element)

        # Merge 2 dicts
        restaurant = dict(restaurant_preview, **restaurant_details)
        print(restaurant)
      except Exception as ex:
        print(ex)
        

