
# JSON Normalization for Dataset Creation

This Python script is designed to normalize JSON files for the purpose of creating datasets. It reads JSON files from a source directory, normalizes them according to a specified configuration file, and saves the normalized files to a destination directory.

## Usage

To use this script, ensure you have the source and destination folders as well as the configuration file in the same directory as the script.

The script is to be run with Python and requires no command line options.

```bash
python normalization_tool.py
```

## File Structure

The script assumes that each source file is a list of JSON objects. Each object in the list is normalized according to the configuration file.

The configuration file is a JSON file that defines the structure of the normalized object. Each key in the configuration file corresponds to a key in the normalized object, and the associated value indicates the corresponding key in the source object.

Here's an example of a configuration file:

```json
{
    "Id" : "uuid",
    "date" : "dateTime.Now",
    "name" : "name",
    "categorie": "category",
    "instruction": "instruction",
    "input": "input",
    "output": "output",
    "src": "src"
}
```

In this example, "Id" is associated with a randomly generated UUID, "date" is associated with the current date and time, and the other keys are associated with the corresponding keys in the source object.

## Dependencies

The script requires Python and the following libraries:

- json
- os
- uuid
- datetime

## License

This project is licensed under the MIT License.
