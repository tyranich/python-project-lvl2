
SING_IDENT = 1
DOUBLE_IDENT = 2


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


def stylish(_dict):
    return_str = []
    level = 0

    def create_str(return_str, level, _dict, key=None):
        tabs_two = "  "
        for _ in _dict.keys():
            if _dict[_]["status"] == "dict":
                return_str.append("{}{}: {{\n".format(
                                  tabs_two * (level + DOUBLE_IDENT), _))
                create_str(return_str, level + 2, get_value(_dict[_]))
                return_str.append("{}}}\n".format(
                                  tabs_two * (level + DOUBLE_IDENT)))
            elif _dict[_]["status"] == "added":
                if isinstance(get_value(_dict[_]), dict):
                    return_str.append("{}+ {}: {{\n".format(
                                      tabs_two * (
                                          level + SING_IDENT), _,))
                    с = "".join(dict_string(get_value(
                                _dict[_]), level + DOUBLE_IDENT))
                    return_str.append("{}".format(с))
                else:
                    return_str.append("{}+ {}: {}\n".format(
                                      tabs_two * (level + SING_IDENT),
                                      _, get_value(_dict[_])))
            elif _dict[_]["status"] == "deleted":
                if isinstance(get_value(_dict[_]), dict):
                    return_str.append("{}- {}: {{\n".format(
                                      tabs_two * (
                                          level + SING_IDENT), _,))
                    с = "".join(dict_string(get_value(_dict[_]),
                                level + DOUBLE_IDENT))
                    return_str.append("{}".format(с))
                else:
                    return_str.append("{}- {}: {}\n".format(
                                      tabs_two * (level + SING_IDENT),
                                      _, get_value(_dict[_])))
            elif _dict[_]["status"] == "changed":
                if isinstance(_dict[_]["value1"], dict):
                    return_str.append("{}- {}: {{\n".format(
                                      tabs_two * (
                                          level + SING_IDENT), _,))
                    с = "".join(dict_string(_dict[_]["value1"],
                                level + DOUBLE_IDENT))
                    return_str.append("{}".format(с))
                else:
                    return_str.append("{}- {}: {}\n".format(
                                      tabs_two * (level + SING_IDENT),
                                      _, _dict[_]["value1"]))

                if isinstance(_dict[_]["value2"], dict):
                    return_str.append("{}+ {}: {{\n".format(
                                      tabs_two * (level + SING_IDENT), _,))
                    с = "".join(dict_string(_dict[_]["value2"],
                                level + DOUBLE_IDENT))
                    return_str.append("{}".format(с))
                else:
                    return_str.append("{}+ {}: {}\n".format(
                                      tabs_two * (level + SING_IDENT),
                                      _, _dict[_]["value2"]))
            elif _dict[_]["status"] == "not changed":
                return_str.append("{}{}: {}\n".format(
                                  tabs_two * (level + DOUBLE_IDENT),
                                  _, get_value(_dict[_])))
        return return_str
    return create_str(return_str, level, _dict)
