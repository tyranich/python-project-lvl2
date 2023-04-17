from gendiff.getters import changed_for_json


FOUR_INDIEND = "    "
TWO_INDIEND = "  "
SIGN_TYPE = {"added": "+", "deleted": "-", "not changed": " "}


def to_string(key, val, depth, return_list: list, symbol=""):
    if isinstance(val, dict):
        return_list.append("{}{}{} {}: {{".
                           format(FOUR_INDIEND * depth,
                                  TWO_INDIEND, symbol, key))
        depth += 1
        for key_in, val_in in val.items():
            to_string(key_in, val_in, depth, return_list, " ")
        return_list.append("{}}}".format(FOUR_INDIEND * depth))
        depth -= 1
    else:
        return_list.append("{}{}{} {}: {}".format(FOUR_INDIEND * depth,
                                                  TWO_INDIEND,
                                                  symbol, key, val))


def raw_stylish(_dict, return_string: list, depth=0):
    for key in _dict.keys():
        if _dict[key]["type"] == "dict":
            depth += 1
            indient = FOUR_INDIEND * (depth)
            return_string.append(f"{indient}{key}: {'{'}")
            value = _dict[key]['value']
            raw_stylish(value, return_string, depth=depth)
            depth -= 1
            return_string.append(f"{indient}{'}'}")

        elif _dict[key]["type"] == "changed":
            to_string(key, changed_for_json(_dict[key]["value1"]),
                      depth, return_string, SIGN_TYPE["deleted"])

            to_string(key, changed_for_json(_dict[key]["value2"]),
                      depth, return_string, SIGN_TYPE["added"])

        else:
            type = _dict[key]["type"]
            to_string(key, changed_for_json(_dict[key]["value"]),
                      depth, return_string, SIGN_TYPE[type])


def stylish(tree):
    result_stylish = list()
    result_stylish.append("{")
    raw_stylish(tree, result_stylish)
    result_stylish.append("}")
    return "\n".join(result_stylish)
