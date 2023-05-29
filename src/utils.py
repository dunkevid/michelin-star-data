def get_michelin_star_data_path(star_num, extension = 'json'):
  path = './data/michelin-star/{}-star.{}'.format(star_num, extension)
  return path
