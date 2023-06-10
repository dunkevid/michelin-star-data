import os
import json

from src.utils.logger import logger
from src.utils.check_file_exists import is_file_exists
from src.utils.get_file_path import get_or_create_aggregator_file_path, get_or_create_change_logs_file_path

def write_data_to_json_file(data, path):
  if not is_file_exists(path):
    f = open(path, 'x')
    f.close()

  with open(path, 'r+', encoding='utf-8') as file:
    if os.path.getsize(path) > 2:
      file_data = json.load(file)
      file_data.extend(data)
      file.seek(0)
      json.dump(file_data, file, indent=2, ensure_ascii=False)
    else:
      json.dump(data, file, indent=2, ensure_ascii=False)

def write_aggregated_df_to_aggregator_csv_file(date, df):
  path = get_or_create_aggregator_file_path()
  
  total_values = df['total'].values
  change_values = df['change'].values
  
  values_str = ','.join(map(str, [*total_values, *change_values]))
  values_str = '{},{}'.format(date, values_str)
  
  try:
    with open(path, 'a') as file:
      row = values_str + '\n'
      file.write(row)
  
    return True
  except Exception as ex:
    logger.error(ex)
    return False

def write_diff_df_to_change_logs_csv_file(date, df):
  path = get_or_create_change_logs_file_path()

  # Extract the values from the dataframe
  name = df['name'].values[0]
  previous_star = df['previous_star'].values[0]
  is_new_restaurant = df['is_new_restaurant'].values[0]
  is_removed = df['is_removed'].values[0]
  increase_star_num = df['increase_star_num'].values[0]

  values_str = f"{date},'{name}',{previous_star},{is_new_restaurant},{is_removed},{increase_star_num}"

  try:
    with open(path, 'a') as file:
      row = values_str + '\n'
      file.write(row)
    return True
  except Exception as ex:
    logger.error(ex)
    return False