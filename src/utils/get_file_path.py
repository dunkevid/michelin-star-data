import glob
import os

from src.utils.check_file_exists import is_file_exists
from src.utils.get_csv_header import get_aggregator_header_str, get_change_logs_header_str

MICHELIN_STAR_DATA_FOLDER = './data/michelin-star'

def get_michelin_star_data_file_path(date, extension = 'json'):
  path = '{}/{}.{}'.format(MICHELIN_STAR_DATA_FOLDER, date, extension)
  return path

def get_latest_michelin_data_file_path():
  list_of_files = glob.glob('{}/*'.format(MICHELIN_STAR_DATA_FOLDER))
  latest_file = max(list_of_files, key=os.path.getctime)

  return latest_file

def get_or_create_aggregator_file_path():
  path = './data/aggregator.csv'

  if not is_file_exists(path):
    header_str = get_aggregator_header_str()
    # Create file and write header
    f = open(path, 'x')
    f.write(header_str)
    f.write('\n')
    f.close()

  return path

def get_or_create_change_logs_file_path():
  path = './data/change_logs.csv'

  if not is_file_exists(path):
    header_str = get_change_logs_header_str()
    # Create file and write header
    f = open(path, 'x')
    f.write(header_str)
    f.write('\n')
    f.close()

  return path

def get_gcb_credential_file_path():
  path = './credential/gcb-credentials.json'

  return path
