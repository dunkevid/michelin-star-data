def _get_number_restaurant_from_str(str):
  str = str.strip()
  start = str.find('of') + 3
  end = str.find('restaurants', start)
  number_restaurant = int(str[start:end].replace(',', '').replace('.', '').strip())
  return number_restaurant

def get_total_restaurants(html):
  element = html.find('h1')
  total_restaurants = _get_number_restaurant_from_str(element.text)

  return total_restaurants
