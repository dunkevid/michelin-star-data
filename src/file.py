import os
import json

def write_data_to_json_file(new_data, path):
  with open(path, 'r+', encoding='utf-8') as file:
    if os.path.getsize(path) > 2:
      file_data = json.load(file)
      file_data.extend(new_data)
      file.seek(0)
      json.dump(file_data, file, indent=2)
    else:
      json.dump(new_data, file, indent=2)
