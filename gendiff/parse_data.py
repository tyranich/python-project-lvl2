import json
import yaml


def open_data(data, format_data):

    if format_data == "json":
        json_return = json.loads(data)
        return json_return
    elif format_data == 'yaml':
        yaml_return = yaml.load(data, yaml.SafeLoader)
        return yaml_return
