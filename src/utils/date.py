from datetime import datetime, timedelta
from src.utils.constants import DATE_FORMAT

def get_date_before(current_date_str):
  current_date = datetime.strptime(current_date_str, DATE_FORMAT)

  date_before = current_date - timedelta(days=1)
  date_before_str = date_before.strftime(DATE_FORMAT)

  return date_before_str
