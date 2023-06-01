from bs4 import BeautifulSoup
from src.constants import HTML_CLASS_NAME

def get_list_restaurant_elements(res_restaurant_list):
  soup = BeautifulSoup(res_restaurant_list, 'lxml')
  list_restaurant_elements = soup.find_all(
    'div',
    class_=HTML_CLASS_NAME['list_restaurants']
  )

  return list_restaurant_elements

def get_restaurant_details_element(res_restaurant_details):
  soup = BeautifulSoup(res_restaurant_details, 'lxml')
  restaurant_details_element = soup.find(
    'div',
    class_=HTML_CLASS_NAME['d_r_details']
  )

  return restaurant_details_element

def get_total_restaurants_element(res_restaurant_list):
  soup = BeautifulSoup(res_restaurant_list, 'lxml')
  total_restaurants_element = soup.find(
    'div',
    class_=HTML_CLASS_NAME['total_restaurants']
  )

  return total_restaurants_element
