def get_michelin_star_data_file_path(date, extension = 'json'):
  path = './data/michelin-star/{}.{}'.format(date, extension)
  return path
