from main import main as start_crawl_data
from src.utils.check_file_exists import is_file_exists
from src.utils.get_current_date_str import get_current_date_str
from src.utils.get_file_path import get_michelin_star_data_file_path
from src.utils.logger import logger

current_date = get_current_date_str()
file_path = get_michelin_star_data_file_path(current_date)

if is_file_exists(file_path):
  logger.warning('Data for {} already exists.'.format(current_date))
else:
  start_crawl_data()
