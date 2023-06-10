import os
from datetime import datetime

from src.utils.get_file_path import MICHELIN_STAR_DATA_FOLDER
from src.utils.constants import DATE_FORMAT

def get_unsync_dates(latest_sync_date_str):
  latest_sync_date = datetime.strptime(latest_sync_date_str, DATE_FORMAT)
  list_of_data_files = os.listdir(MICHELIN_STAR_DATA_FOLDER)

  list_of_data_files = [file_name.split('.json')[0] for file_name in list_of_data_files]
  list_of_data_files_sorted = sorted(list_of_data_files, key=lambda x: x)

  list_of_dates_unsync = []

  for date_str in list_of_data_files_sorted:
    if datetime.strptime(date_str, DATE_FORMAT) > latest_sync_date:
      list_of_dates_unsync.append(date_str)

  return list_of_dates_unsync
