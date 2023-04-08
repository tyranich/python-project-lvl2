from gendiff.getters import changed_for_json


FOUR_INDIEND = "    "
TWO_INDIEND = "  "
SIGN_TYPE = {"added": "+", "deleted": "-", "not changed": " "}


def to_string(key, val, depth, symbol="", return_list=[]):
    if isinstance(val, dict):
        return_list.append("{}{}{} {}: {{".
                           format(FOUR_INDIEND * depth,
                                  TWO_INDIEND, symbol, key))
        depth += 1
        for key_in, val_in in val.items():
            to_string(key_in, val_in, depth, " ", return_list)
        return_list.append("{}}}".format(FOUR_INDIEND * depth))
        depth -= 1
    else:
        return_list.append("{}{}{} {}: {}".format(FOUR_INDIEND * depth,
                                                  TWO_INDIEND,
                                                  symbol, key, val))
    return return_list


def raw_stylish(_dict, return_string=[], depth=0):
    for key in _dict.keys():
        if _dict[key]["type"] == "dict":
            depth += 1
            indient = FOUR_INDIEND * (depth)
            return_string.append(f"{indient}{key}: {'{'}")
            value = _dict[key]['value']
            return_string.extend(raw_stylish(value,
                                             return_string=[],
                                             depth=depth))
            depth -= 1
            return_string.append(f"{indient}{'}'}")

        elif _dict[key]["type"] == "changed":
            value1 = to_string(key, changed_for_json(_dict[key]["value1"]),
                               depth, SIGN_TYPE["deleted"],
                               return_list=[])
            value2 = to_string(key, changed_for_json(_dict[key]["value2"]),
                               depth, SIGN_TYPE["added"],
                               return_list=[])
            return_string.extend(value1)
            return_string.extend(value2)

        else:
            type = _dict[key]["type"]
            value = to_string(key, changed_for_json(_dict[key]["value"]),
                              depth, SIGN_TYPE[type], return_list=[])
            return_string.extend(value)
    return return_string


def stylish(tree):
    result_stylish = list()
    result_stylish.append("{")
    result_stylish.extend(raw_stylish(tree))
    result_stylish.append("}")
    return "\n".join(result_stylish)
