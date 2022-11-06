def changed_for_json(val):
    if val is True:
        return "true"
    elif val is None:
        return "null"
    elif val is False:
        return "false"
    else:
        return val


def get_value(dict_):
    check_json_form = changed_for_json(dict_['value'])
    return check_json_form


def get_children(dict_):
    return {x: val for x, val in dict_.items()}