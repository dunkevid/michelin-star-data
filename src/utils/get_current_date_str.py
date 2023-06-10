from datetime import date
from src.utils.constants import DATE_FORMAT

def get_current_date_str():
  date_str = date.today().strftime(DATE_FORMAT)

  return date_str
