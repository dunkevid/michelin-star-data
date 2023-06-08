from datetime import date

def get_current_date_str():
  date_format = '%Y-%m-%d'
  date_str = date.today().strftime(date_format)

  return date_str
