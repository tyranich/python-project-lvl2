from getters import changed_for_json, get_value, get_children

SING_IDENT = 1
DOUBLE_IDENT = 2
TABS_TWO = "  "


def get_name(dict_):
    for _, _1 in dict_.items():
        return _


def dict_string(dict_, level):
    str_ = []
    tabs = "  "

    def inner(dict1, level_, string_):
        childs = get_children(dict1)
        level_ += 2
        for _ in childs:

            if isinstance(childs[_], dict):
                string_.append((tabs * level_) + _ + ": {\n")
                inner(childs[_], level_, string_)
            else:
                string_.append((tabs * (level_)) + "{}: {}"
                               .format(_, changed_for_json(childs[_])) + "\n")
        level_ -= 1
        string_.append(tabs * (level_ - 1) + "}\n")
        return string_
    return inner(dict_, level, str_)


def if_added(changeable_str, dict_proces, level, name):
    if isinstance(get_value(dict_proces), dict):
        changeable_str.append("{}+ {}: {{\n".format(
                              TABS_TWO * (level + SING_IDENT), name,))
        с = "".join(dict_string(get_value(
                    dict_proces), level + DOUBLE_IDENT))
        changeable_str.append("{}".format(с))
    else:
        changeable_str.append("{}+ {}: {}\n".format(
                              TABS_TWO * (level + SING_IDENT),
                              name, get_value(dict_proces)))


def if_deleted(changeable_str, dict_proces, level, name):
    if isinstance(get_value(dict_proces), dict):
        changeable_str.append("{}- {}: {{\n".format(
                              TABS_TWO * (level + SING_IDENT), name,))
        с = "".join(dict_string(get_value(dict_proces),
                    level + DOUBLE_IDENT))
        changeable_str.append("{}".format(с))
    else:
        changeable_str.append("{}- {}: {}\n".format(
                              TABS_TWO * (level + SING_IDENT),
                              name, get_value(dict_proces)))


def if_changed(changeable_str, dict_proces, level, name):
    if isinstance(dict_proces["value1"], dict):
        changeable_str.append("{}- {}: {{\n".format(
                              TABS_TWO * (level + SING_IDENT), name,))
        с = "".join(dict_string(dict_proces["value1"],
                    level + DOUBLE_IDENT))
        changeable_str.append("{}".format(с))
    else:
        changeable_str.append("{}- {}: {}\n".format(
                              TABS_TWO * (level + SING_IDENT),
                              name, changed_for_json(dict_proces["value1"])))
    if isinstance(dict_proces["value2"], dict):
        changeable_str.append("{}+ {}: {{\n".format(
                              TABS_TWO * (level + SING_IDENT), name,))
        с = "".join(dict_string(dict_proces["value2"],
                    level + DOUBLE_IDENT))
        changeable_str.append("{}".format(с))
    else:
        changeable_str.append("{}+ {}: {}\n".format(
                              TABS_TWO * (level + SING_IDENT),
                              name, changed_for_json(dict_proces["value2"])))


def if_not_changed(changeable_str, dict_proces, level, name):
    changeable_str.append("{}{}: {}\n".format(
                          TABS_TWO * (level + DOUBLE_IDENT),
                          name, get_value(dict_proces)))


def chose_status(dict_status, changeable_str, dict_proces, level, name):

    if dict_status == "added":
        return_function = if_added(changeable_str, dict_proces, level, name)
    elif dict_status == "deleted":
        return_function = if_deleted(changeable_str, dict_proces, level, name)
    elif dict_status == "changed":
        return_function = if_changed(changeable_str, dict_proces, level, name)
    elif dict_status == "not changed":
        return_function = if_not_changed(changeable_str,
                                         dict_proces, level, name)

    return return_function


def stylish(_dict):
    return_str = ["{    \n"]
    level = 0
    def create_str(return_str, level, _dict, key=None):
        
        for _ in _dict.keys():
            if _dict[_]["status"] == "dict":
                return_str.append("{}{}: {{\n".format(
                                  TABS_TWO * (level + DOUBLE_IDENT), _))
                create_str(return_str, level + 2, get_value(_dict[_]))
                return_str.append("{}}}\n".format(
                                  TABS_TWO * (level + DOUBLE_IDENT)))
            else:
                chose_status(_dict[_]["status"], return_str, _dict[_], level, _)
        if level == 0:
            return_str.append("}")
        return return_str
    return create_str(return_str, level, _dict)
