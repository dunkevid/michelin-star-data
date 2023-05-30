import json
from src.utils import get_michelin_star_data_path

NUMBER_OF_MICHELIN_STAR = 3
CSV_FILE_PATH = './data/michelin-star/restaurants.csv'

HEADER_LIST = [
  'name', # string
  'year', # number
  'star', # number
  'is_green_star', # boolean
  'is_bib_gourmand', # boolean
  'type', # string
  'region', # string
  'city', # string
  'address', # string
  'latitude', # string
  'longtitude', # string
  'price_symbol', # string
  'price_rate', # number
  'description', # string
  'phone', # string
  'website', # string
  'image_thumb', # string
  'opening_hours', # list[string]
  'services', # list[string]
  'link' # string
]
header_list_str = ','.join(item for item in HEADER_LIST)

def transform_array_to_string(arr):
  str_arr = [
    f'"{item}"'
    if isinstance(item, str) or isinstance(item, list)
    else str(item) for item in arr
  ]
  return ','.join(str_arr)

def normalize_restaurant_data(r):
  name = r['name']
  year = int(r['updated_at'][-4:])
  star = r['awards']['star']
  is_green_star = r['awards']['is_green_star']
  is_bib_gourmand = r['awards']['is_bib_gourmand']
  type = r['type']
  region = r['coords']['short_location_name'].split(',')[-1].strip()
  city = r['coords']['short_location_name'].split(',')[0].strip()
  address = r['address']
  latitude = r['coords']['lat']
  longtitude = r['coords']['lng']
  price_symbol = r['price']['symbol']
  price_rate = r['price']['rate']
  description = r['description'].replace("\"", '\'')
  phone = r['phone']
  website = r['website']
  image_thumb = r['image_thumb']
  opening_hours = r['opening_hours']
  services = r['facilities_and_services']
  link = r['link_to_detail_url']

  row_normalized = transform_array_to_string([
    name,
    year,
    star,
    is_green_star,
    is_bib_gourmand,
    type,
    region,
    city,
    address,
    latitude,
    longtitude,
    price_symbol,
    price_rate,
    description,
    phone,
    website,
    image_thumb,
    opening_hours,
    services,
    link
  ])

  return row_normalized

def to_csv():
  all_restaurants = []
  for i in range(1, NUMBER_OF_MICHELIN_STAR + 1):
    path = get_michelin_star_data_path(i)
    with open(path, 'r', encoding='utf-8') as file:
      data = json.load(file)
      all_restaurants += data

  with open(CSV_FILE_PATH, 'w') as file:
    file.write(header_list_str)
    file.write('\n')
    for restaurant in all_restaurants:
      row = normalize_restaurant_data(restaurant) + '\n'
      file.write(row)

  print('✨ Done')

to_csv()
