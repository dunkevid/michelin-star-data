import json
import pandas as pd
from src.utils.get_file_path import \
  get_latest_michelin_data_file_path, \
  get_or_create_aggregator_file_path, \
  get_or_create_change_logs_file_path

def get_latest_restaurants_df():
  path = get_latest_michelin_data_file_path()

  with open(path) as file:
    json_data = json.load(file)

  df = pd.json_normalize(json_data)

  df.rename(
    columns={
      'price.raw': 'price_raw',
      'price.symbol': 'price_currency',
      'price.rate': 'price_rate',
      'awards.star': 'star',
      'awards.is_green_star': 'is_green_star',
      'awards.is_bib_gourmand': 'is_bib_gourmand',
      'position.latitude': 'latitude',
      'position.longtitude': 'longtitude',
      'position.location.region': 'region',
      'position.location.city': 'city',
    },
    inplace=True
  )

  return df

def get_aggregated_data_df():
  path = get_or_create_aggregator_file_path()
  df = pd.read_csv(path)

  return df

def get_change_logs_data_df():
  path = get_or_create_change_logs_file_path()
  df = pd.read_csv(path)

  return df
 