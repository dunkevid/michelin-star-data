import json

def write_data_to_json_file(data, path):
  with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
