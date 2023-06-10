def get_aggregator_header_str():
  AGGREGATOR_HEADER_LIST = [
    'date',
    'total_1',
    'total_2',
    'total_3',
    'change_1',
    'change_2',
    'change_3'
  ]
  header_str = ','.join(item for item in AGGREGATOR_HEADER_LIST)

  return header_str

def get_change_logs_header_str():
  CHANGE_LOGS_HEADER_LIST = [
    'date',
    'name',
    'previous_star',
    'is_new_restaurant',
    'is_removed',
    'increase_star_num'
  ]
  header_str = ','.join(item for item in CHANGE_LOGS_HEADER_LIST)

  return header_str
