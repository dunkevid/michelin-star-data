import json
from src.utils import get_michelin_star_data_path

header_list ='name,address,address_short,description,phone,website,image_thumb,price_symbol,price_rate,type,star,is_green_star,is_bib_gourmand,coord_lat,coord_lng,opening_hours,services,michelin_link,created_at,updated_at'

NUMBER_OF_MICHELIN_STAR = 3
all_restaurants = []
for i in range(1, NUMBER_OF_MICHELIN_STAR + 1):
  path = get_michelin_star_data_path(i)
  with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    all_restaurants += data

with open('./data/michelin-star/restaurants.csv', 'w') as file:
  file.write(header_list)
  file.write('\n')
  for r in all_restaurants:
    file.write('"{}","{}","{}","{}","{}","{}","{}","{}",{},"{}",{},{},{},"{}","{}","{}","{}","{}","{}","{}"\n'.format(
      r['name'],
      r['address'],
      r['coords']['short_location_name'],
      r['description'].replace("\"", '\''),
      r['phone'],
      r['website'],
      r['image_thumb'],
      r['price']['symbol'],
      r['price']['rate'],
      r['type'],
      r['awards']['star'],
      r['awards']['is_green_star'],
      r['awards']['is_bib_gourmand'],
      r['coords']['lat'],
      r['coords']['lng'],
      r['opening_hours'],
      r['facilities_and_services'],
      r['link_to_detail_url'],
      r['created_at'],
      r['updated_at']
    ))
