from bs4 import BeautifulSoup
from src.utils.constants import HTML_CLASS_NAME, ROOT_URL

def get_restaurant_name(html):
  element = html.find('h3', class_=HTML_CLASS_NAME['l_r_name'])
  name = element.text.strip()

  return name

def get_restaurant_image_thumb(html):
  element = html.find('a', class_=HTML_CLASS_NAME['l_r_image_thumb'])
  image_thumb = element.get('ci-bg-url')

  return image_thumb

def get_restaurant_awards(html):
  img_elements = html.find_all('img', class_=HTML_CLASS_NAME['l_r_award'])

  star_award_str = '1star'
  green_star_award_str = 'gastronomie'
  bib_award_str = 'bib'
  
  star_num = 0
  is_have_green_star = False
  is_have_bib_gourmand = False
  
  for i in img_elements:
    if i.get('class')[0] == 'michelin-award':
      img_src = i.get('src')
      if star_award_str in img_src:
        star_num += 1
      if green_star_award_str in img_src:
        is_have_green_star = True
      if bib_award_str in img_src:
        is_have_bib_gourmand = True

  return {
    'star': star_num,
    'is_green_star': is_have_green_star,
    'is_bib_gourmand': is_have_bib_gourmand,
  }

def get_restaurant_price(html):
  element = html.find('div', class_=HTML_CLASS_NAME['l_r_price'])
  price = element.text.strip().split('\n')[0]

  return {
    'raw': price,
    'symbol': price[0],
    'rate': len(price)
  }

def get_restaurant_coordinates(html):
  html = BeautifulSoup(str(html), 'lxml')
  short_location_element = html.find('div', class_=HTML_CLASS_NAME['l_r_short_location'])
  coords_element = html.find('div', class_=HTML_CLASS_NAME['l_r_coords'])

  short_location_name = short_location_element.text.strip()

  return {
    'location': {
      'region': short_location_name.split(',')[-1].strip(),
      'city': short_location_name.split(',')[0].strip()
    },
    'latitude': coords_element.get('data-lat'),
    'longtitude': coords_element.get('data-lng')
  }

def get_restaurent_type(html):
  element = html.find('div', class_=HTML_CLASS_NAME['l_r_type'])
  
  _tmp_str_arr = element.text.replace(' ', '').strip().split('\n')
  restaurent_type = _tmp_str_arr[len(_tmp_str_arr) - 1]
  
  return restaurent_type

def get_retaurent_detail_url(html):
  element = html.find('a', class_=HTML_CLASS_NAME['l_r_link_to_detail_page'])
  href = element.get('href')

  detail_url = '{}{}'.format(ROOT_URL, href)

  return detail_url
