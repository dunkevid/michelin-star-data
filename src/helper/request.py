import requests

from src.utils.logger import logger
from src.utils.get_michelin_url import get_michelin_url
from src.utils.user_agent_proxy import get_headers_with_random_user_agent

def _get_request(url, retry_time = 0):
  if retry_time >= 3:
    return False
  
  if retry_time > 0:
    logger.warning('Retry to {} ({})'.format(url, retry_time))
  
  try:
    headers = get_headers_with_random_user_agent()
    proxy = ''
    req = requests.get(url, headers=headers, proxies=proxy)
    return req.text
  except Exception as ex:
    logger.error('[ERROR] {}'.format(ex))
    retry_time += 1
    return _get_request(url, retry_time)

def request_to_restaurant_list_page(star_num = 1, page = 1):
  url = get_michelin_url(star_num, page)
  
  req = _get_request(url)
  return req

def request_to_restaurant_details_page(detail_url):
  req = _get_request(detail_url)

  return req
