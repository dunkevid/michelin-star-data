import pandas as pd
from src.utils.get_file_path import get_michelin_star_data_file_path
from src.utils.date import get_date_before

def _get_michelin_data_by_date(date):
  try:
    path = get_michelin_star_data_file_path(date)
    df = pd.read_json(path)

    df['star'] = df['awards'].apply(lambda x: x['star'])
    # df['is_green_star'] = df['awards'].apply(lambda x: x['is_green_star'])
    # df['is_bib_gourmand'] = df['awards'].apply(lambda x: x['is_bib_gourmand'])

    selected_list = [
      'name',
      'star',
      # 'is_green_star',
      # 'is_bib_gourmand'
    ]

    return df[selected_list]
  except:
    return False

def _count_total_star(df):
  size_sf = df.groupby('star').size()
  df =  pd.DataFrame({
    'star': size_sf.index,
    'total': size_sf.values
  })
  
  return df

def get_diff_data(date):
  df = _get_michelin_data_by_date(date)
  df_before = _get_michelin_data_by_date(get_date_before(date))

  if isinstance(df_before, pd.DataFrame):
    def _is_new_restaurant(name):
      is_new = len(df_before.loc[df_before['name'] == name]) == 0
      return is_new
    
    def _is_removed(name):
      is_removed = len(df_before.loc[df_before['name'] == name]) > 0 \
        and len(df.loc[df['name'] == name]) == 0
      return is_removed

    def _get_previous_star(x):
      if x['is_new_restaurant']:
        return 0
      else:
        previous_star = df_before.loc[df_before['name'] == x['name']]['star'].values[0]
        return previous_star
    
    def _get_increase_star_num(x):
      if x['is_new_restaurant']:
        return x['star']
      elif x['is_removed']:
        return -x['previous_star']
      else:
        return x['star'] - x['previous_star']
    
    diff = pd.concat([df, df_before]).drop_duplicates(keep=False)
    
    diff['is_new_restaurant'] = diff.apply(
      lambda x: _is_new_restaurant(x['name']),
      axis=1
    )

    diff['is_removed'] = diff.apply(
      lambda x: _is_removed(x['name']),
      axis=1
    )

    diff['previous_star'] = diff.apply(
      lambda x: _get_previous_star(x),
      axis=1
    )
    
    diff['increase_star_num'] = diff.apply(
      lambda x: _get_increase_star_num(x),
      axis=1
    )

    selected = ['name', 'previous_star', 'is_new_restaurant', 'is_removed', 'increase_star_num']
    
    return diff[selected]

def get_michelin_aggregate_data(date):
  df = _get_michelin_data_by_date(date)
  df_before = _get_michelin_data_by_date(get_date_before(date))

  total_star_df = _count_total_star(df)
  total_star_df_before = _count_total_star(df_before) \
    if isinstance(df_before, pd.DataFrame) \
    else pd.DataFrame({'star': [1, 2, 3], 'total': [0, 0, 0]})

  total_star_df['change'] = total_star_df['total'] - total_star_df_before['total']

  return total_star_df
