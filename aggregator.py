from src.utils.logger import logger
from src.utils.get_latest_synced_date import get_latest_synced_date
from src.helper.sync_aggregate_data import sync_aggregate_data

def aggregator():
  latest_synced_date = get_latest_synced_date()
  sync_aggregate_data(latest_synced_date)
  logger.info('✨ Done')

aggregator()
