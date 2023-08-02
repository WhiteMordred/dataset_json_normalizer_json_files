import os
import uuid
from datetime import datetime
import pandas as pd
import json
import argparse

def normalize(src_dir, dest_dir, config_path, input_extension, output_extension):
    # Load the config file
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Define the input and output methods based on the extensions
    load_method = pd.read_json if input_extension == 'json' else pd.read_csv
    save_method = pd.DataFrame.to_json if output_extension == 'json' else pd.DataFrame.to_csv

    # Iterate through all the files in the source directory
    for filename in os.listdir(src_dir):
        if filename.endswith('.' + input_extension):
            # Load the source file
            df = load_method(os.path.join(src_dir, filename))

            new_data_list = []
            for _, row in df.iterrows():
                data = row.to_dict()
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

            # Convert the list of dictionaries to a DataFrame
            df = pd.DataFrame(new_data_list)

            # Save the DataFrame to a file in the destination directory
            save_method(df, os.path.join(dest_dir, filename.replace('.' + input_extension, '.' + output_extension)), index=False)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Normalize datasets.')
    parser.add_argument('--ext_src', type=str, help='Source file extension (json or csv)', required=True)
    parser.add_argument('--ext_dest', type=str, help='Destination file extension (json or csv)', required=True)
    args = parser.parse_args()

    # Get the current script directory
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # Define the source, destination, and config paths
    src_dir = os.path.join(current_dir, 'src')
    dest_dir = os.path.join(current_dir, 'dest')
    config_path = os.path.join(current_dir, 'config.json')

    normalize(src_dir, dest_dir, config_path, args.ext_src, args.ext_dest)
