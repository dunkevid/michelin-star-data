import pandas as pd

from src.helper.file import write_aggregated_df_to_aggregator_csv_file, write_diff_df_to_change_logs_csv_file
from src.utils.get_unsync_dates import get_unsync_dates
from src.utils.get_aggregate_data import get_michelin_aggregate_data, get_diff_data

def sync_aggregate_data(latest_sync_date):
  unsync_dates = get_unsync_dates(latest_sync_date)

  for unsync_date_str in unsync_dates:
    agrregated_df = get_michelin_aggregate_data(unsync_date_str)
    write_aggregated_df_to_aggregator_csv_file(unsync_date_str, agrregated_df)
    diff_df = get_diff_data(unsync_date_str)
    if isinstance(diff_df, pd.DataFrame) and len(diff_df) > 0:
      write_diff_df_to_change_logs_csv_file(unsync_date_str, diff_df)
