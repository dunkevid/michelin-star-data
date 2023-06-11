from google.cloud import bigquery

from src.config.google_bigquery import client
from src.utils.logger import logger

def gcb_load_df(table_id, df):
  try:
    job_config = bigquery.LoadJobConfig(
      schema=[],
      write_disposition='WRITE_TRUNCATE'
    )

    # Make an API request.
    job = client.load_table_from_dataframe(
      df,
      table_id,
      job_config=job_config
    )
    # Wait for the job to complete.
    job.result()  

    # Make an API request.
    table = client.get_table(table_id)  
    logger.info(
      'Loaded {} rows and {} columns to {}'.format(
        table.num_rows, len(table.schema), table_id
      )
    )

    return True
  except Exception as ex:
    logger.error(ex)
    return False
