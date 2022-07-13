SING_IDENT = 1
DOUBLE_IDENT = 2
TABS_TWO = "  "


def get_children(dict_):
    return {x: val for x, val in dict_.items()}


def get_name(dict_):
    for _, _1 in dict_.items():
        return _


def get_value(dict_):
    return dict_['value']


def dict_string(dict_, level):
    str_ = []
    tabs = "  "

    def test_(dict1, level_, string_):
        childs = get_children(dict1)
        level_ += 2
        for _ in childs:

            if isinstance(childs[_], dict):
                string_.append((tabs * level_) + _ + ": {\n")
                test_(childs[_], level_, string_)
            else:
                string_.append((tabs * (level_)) + "{}: {}"
                               .format(_, childs[_]) + "\n")
        level_ -= 1
        string_.append(tabs * (level_ - 1) + "}\n")
        return string_
    return test_(dict_, level, str_)


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
    if isinstance(dict_proces[name]["value1"], dict):
        changeable_str.append("{}- {}: {{\n".format(
                              TABS_TWO * (level + SING_IDENT), name,))
        с = "".join(dict_string(dict_proces[name]["value1"],
                    level + DOUBLE_IDENT))
        changeable_str.append("{}".format(с))
    else:
        changeable_str.append("{}- {}: {}\n".format(
                              TABS_TWO * (level + SING_IDENT),
                              name, dict_proces[name]["value1"]))

    if isinstance(dict_proces[name]["value2"], dict):
        changeable_str.append("{}+ {}: {{\n".format(
                              TABS_TWO * (level + SING_IDENT), name,))
        с = "".join(dict_string(dict_proces[name]["value2"],
                    level + DOUBLE_IDENT))
        changeable_str.append("{}".format(с))
    else:
        changeable_str.append("{}+ {}: {}\n".format(
                              TABS_TWO * (level + SING_IDENT),
                              name, dict_proces[name]["value2"]))


def stylish(_dict):
    return_str = []
    level = 0

    def create_str(return_str, level, _dict, key=None):
        for _ in _dict.keys():
            if _dict[_]["status"] == "dict":
                return_str.append("{}{}: {{\n".format(
                                  TABS_TWO * (level + DOUBLE_IDENT), _))
                create_str(return_str, level + 2, get_value(_dict[_]))
                return_str.append("{}}}\n".format(
                                  TABS_TWO * (level + DOUBLE_IDENT)))

            elif _dict[_]["status"] == "added":
                if_added(return_str, _dict[_], level, _)
                """
                if isinstance(get_value(_dict[_]), dict):
                    return_str.append("{}+ {}: {{\n".format(
                                      TABS_TWO * (
                                          level + SING_IDENT), _,))
                    с = "".join(dict_string(get_value(
                                _dict[_]), level + DOUBLE_IDENT))
                    return_str.append("{}".format(с))
                else:
                    return_str.append("{}+ {}: {}\n".format(
                                      TABS_TWO * (level + SING_IDENT),
                                      _, get_value(_dict[_])))
                """
            elif _dict[_]["status"] == "deleted":
                if_deleted(return_str, _dict[_], level, _)
                """
                if isinstance(get_value(_dict[_]), dict):
                    return_str.append("{}- {}: {{\n".format(
                                      TABS_TWO * (
                                          level + SING_IDENT), _,))
                    с = "".join(dict_string(get_value(_dict[_]),
                                level + DOUBLE_IDENT))
                    return_str.append("{}".format(с))
                else:
                    return_str.append("{}- {}: {}\n".format(
                                      TABS_TWO * (level + SING_IDENT),
                                      _, get_value(_dict[_])))
                """
            elif _dict[_]["status"] == "changed":
                if_changed(return_str, _dict, level, _)
                """
                if isinstance(_dict[_]["value1"], dict):
                    return_str.append("{}- {}: {{\n".format(
                                      TABS_TWO * (
                                          level + SING_IDENT), _,))
                    с = "".join(dict_string(_dict[_]["value1"],
                                level + DOUBLE_IDENT))
                    return_str.append("{}".format(с))
                else:
                    return_str.append("{}- {}: {}\n".format(
                                      TABS_TWO * (level + SING_IDENT),
                                      _, _dict[_]["value1"]))

                if isinstance(_dict[_]["value2"], dict):
                    return_str.append("{}+ {}: {{\n".format(
                                      TABS_TWO * (level + SING_IDENT), _,))
                    с = "".join(dict_string(_dict[_]["value2"],
                                level + DOUBLE_IDENT))
                    return_str.append("{}".format(с))
                else:
                    return_str.append("{}+ {}: {}\n".format(
                                      TABS_TWO * (level + SING_IDENT),
                                      _, _dict[_]["value2"]))
                """
            elif _dict[_]["status"] == "not changed":
                return_str.append("{}{}: {}\n".format(
                                  TABS_TWO * (level + DOUBLE_IDENT),
                                  _, get_value(_dict[_])))
        return return_str
    return create_str(return_str, level, _dict)
