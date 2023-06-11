from src.utils.logger import logger
from src.utils.get_df import get_latest_restaurants_df, get_aggregated_data_df, get_change_logs_data_df
from src.helper.gcb import gcb_load_df

DATASET = 'michelin-star-data.michelin_star'
RESTAURANTS_TABLE_ID = '{}.restaurants'.format(DATASET)
AGGREGATOR_TALBE_ID = '{}.aggregator'.format(DATASET)
LOGS_TALBE_ID = '{}.logs'.format(DATASET)

def _load_latest_restaurants():
  latest_restaurants_df = get_latest_restaurants_df()
  load_restaurants_result = gcb_load_df(
    RESTAURANTS_TABLE_ID,
    latest_restaurants_df
  )
  logger.info('Load restaurants result: {}'.format(load_restaurants_result))

def _load_aggregated_data():
  aggregated_data_df = get_aggregated_data_df()
  load_aggregated_data_result = gcb_load_df(
    AGGREGATOR_TALBE_ID,
    aggregated_data_df
  )
  logger.info('Load aggregated data result: {}'.format(load_aggregated_data_result))


def _load_change_logs_data():
  logs_df = get_change_logs_data_df()
  load_logs_result = gcb_load_df(
    LOGS_TALBE_ID,
    logs_df
  )
  logger.info('Load logs result: {}'.format(load_logs_result))

def load_into_gcb():
  _load_latest_restaurants()
  _load_aggregated_data()
  _load_change_logs_data()

load_into_gcb()
