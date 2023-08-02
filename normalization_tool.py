import json
import os
import uuid
from datetime import datetime

def normalize(src_dir, dest_dir, config_path):
    # Load the config file
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Iterate through all the files in the source directory
    for filename in os.listdir(src_dir):
        if filename.endswith('.json'):
            # Load the source file
            with open(os.path.join(src_dir, filename), 'r') as f:
                data_list = json.load(f)

            new_data_list = []
            for data in data_list:
                # Create a new dictionary based on the config
                new_data = {}
                for key, value in config.items():
                    if value == 'uuid':
                        new_data[key] = str(uuid.uuid4())
                    elif value == 'dateTime.Now':
                        new_data[key] = datetime.now().isoformat()
                    elif value in data:
                        new_data[key] = data[value]
                    else:
                        new_data[key] = value

                new_data_list.append(new_data)

            # Save the new data to the destination directory
            with open(os.path.join(dest_dir,"normalized_"+filename), 'w') as f:
                json.dump(new_data_list, f, ensure_ascii=False, indent=4)

# Get the current script directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Define the source, destination, and config paths
src_dir = os.path.join(current_dir, 'src')
dest_dir = os.path.join(current_dir, 'dest')
config_path = os.path.join(current_dir, 'config.json')

normalize(src_dir, dest_dir, config_path)
