from gendiff.scripts.getters import changed_for_json, get_value

def is_string(val):
    if isinstance(val, str):
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

def if_added(level, return_str, dict_, root, name):
    value = is_string(get_value(dict_[name]))
    if level == 0:
        if isinstance(get_value(dict_[name]), dict) or \
                isinstance(get_value(dict_[name]), list):
            value = "[complex value]"
            return_str.append("Property '{}' was added with value: {}\n"
                  .format(name, value))
        else:
            return_str.append("Property '{}' was added with value: {}\n"
                  .format(name, value))
    else:
        if isinstance(get_value(dict_[name]), dict) or \
                isinstance(get_value(dict_[name]), list):
            value = "[complex value]"
            return_str.append("Property '{}.{}' was added with value: {}\n".
                  format(root, name, value))
        else:
            return_str.append("Property '{}.{}' was added with value: {}\n".
                  format(root, name, value))


def if_deleted(level, return_str, root, name):
    if level == 0:
        return_str.append("Property '{}' was removed\n".format(name))
    else:
        return_str.append("Property '{}.{}' was removed\n".format(root, name))


def if_changed(level, return_str, dict_, root, name):
    value1 = is_string(changed_for_json(dict_[name]["value1"]))
    value2 = is_string(changed_for_json(dict_[name]["value2"]))
    if isinstance(dict_[name]["value1"], dict) or \
            isinstance(dict_[name]["value1"], list):
        value1 = '[complex value]'
    if isinstance(dict_[name]["value2"], dict) or \
            isinstance(dict_[name]["value2"], list):
        value2 = '[complex value]'
    return_str.append("Property '{}.{}' was updated. From {} to {}\n".
          format(root, name, value1, value2))


def choise_status(dict_status, return_str, level, dict_, root, name):

    if dict_status == "added":
        if_added(level, return_str, dict_, root, name)
    elif dict_status == "deleted":
        if_deleted(level, return_str, root, name)
    elif dict_status == "changed":
        if_changed(level, return_str, dict_, root, name)


def plain(_dict):
    return_str = []
    level = 0

    def create_str(return_str, level, _dict, name):

        for key in _dict.keys():

            if _dict[key]["status"] == "dict":
                if level == 0:
                    name2 = key
                else:
                    name2 = f"{name}.{key}"
                level += 1
                create_str(return_str, level + 2, get_value(_dict[key]), name2)
                level -= 1
            else:
                choise_status(_dict[key]["status"], return_str, level, _dict, name, key)
        if level == 0:
            return_str[-1] = return_str[-1][:-1]
        return return_str
    return create_str(return_str, level, _dict, "")
