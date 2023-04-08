import json


def changed_for_json(val):
    if isinstance(val, bool) or val is None:
        return json.dumps(val)
    else:
        return val


def get_value(dict_):
    check_json_form = changed_for_json(dict_['value'])
    return check_json_form


def get_children(dict_):
    return {x: val for x, val in dict_.items()}
