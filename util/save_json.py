import json
import os
def save_json(data: dict, directory: str, file_name: str):

  os.makedirs(directory, exist_ok=True)
  
  file_path = os.path.join(directory, file_name)
  
  with open(file_path, 'w') as file:
      json.dump(data, file, indent=2)