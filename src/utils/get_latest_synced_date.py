import pandas as pd

from src.utils.get_file_path import get_or_create_aggregator_file_path

def get_latest_synced_date():
  path = get_or_create_aggregator_file_path()
  df = pd.read_csv(path)

  return df['date'].iloc[-1] if len(df) > 0 else '1999-01-01'
