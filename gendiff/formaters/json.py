import json


def json_formater(dict_):
    data = json.dumps(dict_, indent=4)
    return data
