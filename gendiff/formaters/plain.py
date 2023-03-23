
def to_string(val):

    if isinstance(val, dict) or\
            isinstance(val, list):
        return "[complex value]"

    elif isinstance(val, str):
        if val == "false":
            return val
        elif val == "true":
            return val
        elif val == "null":
            return val
        else:
            return "'{}'".format(val)
    else:
        return val


def changed_for_json(val):
    if val is True:
        return "true"
    elif val is None:
        return "null"
    elif val is False:
        return "false"
    else:
        return val


def plain(_dict):  # noqa: C901
    return_string = []

    def inner(_dict, return_string, next_name=''):
        for key in _dict.keys():
            if _dict[key]["type"] == "dict":
                measure_name = next_name
                value = _dict[key]['value']
                next_name += "{}.".format(key)
                inner(value, return_string, next_name)
                next_name = measure_name
            elif _dict[key]["type"] == "added":
                value = to_string(changed_for_json(_dict[key]["value"]))
                return_string.append(f"Property '{next_name}{key}'"
                                     f" was added with value: {value}")
            elif _dict[key]["type"] == "deleted":
                value = to_string(changed_for_json(_dict[key]["value"]))
                return_string.append(f"Property '{next_name}{key}'"
                                     f" was removed")
            elif _dict[key]["type"] == "changed":
                value1 = to_string(changed_for_json(_dict[key]["value1"]))
                value2 = to_string(changed_for_json(_dict[key]["value2"]))
                return_string.append(f"Property '{next_name}{key}' was "
                                     f"updated. From {value1} to {value2}")
        return return_string

    return "\n".join(inner(_dict, return_string))
