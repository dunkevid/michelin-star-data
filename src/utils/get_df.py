import pandas as pd
from src.utils.get_file_path import \
  get_latest_michelin_data_file_path, \
  get_or_create_aggregator_file_path, \
  get_or_create_change_logs_file_path

def get_latest_restaurants_df():
  path = get_latest_michelin_data_file_path()
  df = pd.read_json(path)

  return df

def get_aggregated_data_df():
  path = get_or_create_aggregator_file_path()
  df = pd.read_csv(path)

  return df

def get_change_logs_data_df():
  path = get_or_create_change_logs_file_path()
  df = pd.read_csv(path)

  return df
 