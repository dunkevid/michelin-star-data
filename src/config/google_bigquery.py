import os
import json
from google.cloud import bigquery
from google.oauth2 import service_account

from src.utils.logger import logger
from src.utils.check_file_exists import is_file_exists
from src.utils.get_file_path import get_gcb_credential_file_path

def _get_credients():
  path = get_gcb_credential_file_path()

  if is_file_exists(path):
    logger.info('GET GCB CREDENTIALS FROM FILE')
    return service_account.Credentials \
      .from_service_account_file(path)
  else:
    logger.info('GET GCB CREDENTIALS FROM SECRET VARIABLES')
    secret_value = os.environ['GCB_CREDENTIALS']
    secret_value_json = json.loads(secret_value)
    return service_account.Credentials \
      .from_service_account_info(secret_value_json)

_project_id = 'michelin-star-data'
_credentials = _get_credients()

client = bigquery.Client(credentials=_credentials, project=_project_id)
