ROOT_URL = 'https://guide.michelin.com'
RESTAURANTS_URL = '{}/at/en/restaurants'.format(ROOT_URL)

HTML_CLASS_NAME = {
  # Restaurant card
  'list_restaurants': 'card__menu box-placeholder js-restaurant__list_item js-match-height js-map',
  'total_restaurants': 'flex-fill search-results__stats js-restaurant__stats pl-text pl-big',

  # Restaurant card item
  'l_r_name': 'card__menu-content--title pl-text pl-big js-match-height-title',
  'l_r_image_thumb': 'image-wrapper pl-image',
  'l_r_award': 'michelin-award',
  'l_r_price': 'card__menu-footer--price pl-text',
  'l_r_short_location': 'card__menu-footer--location flex-fill pl-text',
  'l_r_coords': 'card__menu box-placeholder js-restaurant__list_item js-match-height js-map',
  'l_r_type': 'card__menu-footer--price pl-text',
  'l_r_link_to_detail_page': 'link',

  # Retaurant details
  'd_r_details': 'restaurant-details',
  'd_r_detail_address': 'restaurant-details__heading--address',
  'd_r_detail_description': 'restaurant-details__description--text',
  'd_r_detail_facilities_and_services': 'row restaurant-details__services--list',
  'd_r_detail_information': 'link js-dtm-link', # Phone and Website
  'd_r_detail_opening_hours': 'open__time d-flex',
}

DATE_FORMAT = '%Y-%m-%d'
