import os
from google.cloud import bigquery
from google.oauth2 import service_account

from src.utils.logger import logger
from src.utils.check_file_exists import is_file_exists
from src.utils.get_file_path import get_gcb_credential_file_path

def _get_credients_json():
  path = get_gcb_credential_file_path()

  if is_file_exists(path):
    logger.info('GET GCB CREDENTIALS FROM FILE')
    return path
  else:
    logger.info('GET GCB CREDENTIALS FROM SECRET VARIABLES')
    return os.environ['GCB_CREDENTIALS']

_project_id = 'michelin-star-data'
_credentials_json = _get_credients_json()
_credentials = service_account.Credentials \
  .from_service_account_file(
    _credentials_json
  )

client = bigquery.Client(credentials=_credentials, project=_project_id)
