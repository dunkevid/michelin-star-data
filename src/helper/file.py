import os
import json

def _is_file_exists(path):
  return os.path.isfile(path)

def write_data_to_json_file(data, path):
  if not _is_file_exists(path):
    f = open(path, 'x')
    f.close()

  with open(path, 'r+', encoding='utf-8') as file:
    if os.path.getsize(path) > 2:
      file_data = json.load(file)
      file_data.extend(data)
      file.seek(0)
      json.dump(file_data, file, indent=2, ensure_ascii=False)
    else:
      json.dump(data, file, indent=2, ensure_ascii=False)
