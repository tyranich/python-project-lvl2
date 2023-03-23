from gendiff.getters import changed_for_json


TWO_INDIEND = "  "
SIGN_TYPE = {"added": "+", "deleted": "-", "not changed": " "}


def to_string(val, depth):
    if isinstance(val, dict):
        return_list = []
        return_list.append(f"{'{'}")

        def inner(val, return_list, depth=0):
            depth = depth
            for key in val.keys():
                if isinstance(val[key], dict):
                    indient = (depth + 3) * TWO_INDIEND
                    return_list.append(f"{indient}{key}: {'{'}")
                    depth += 2
                    inner(val[key], return_list, depth)
                    depth -= 2
                else:

                    indient = (depth + 3) * TWO_INDIEND
                    value = val[key]
                    return_list.append(f"{indient}{key}: {value}")
            indient = TWO_INDIEND * (depth + 1)
            return_list.append(f"{indient}{'}'}")
            return return_list
        return "\n".join(inner(val, return_list, depth))
    else:
        return val


def stylish(_dict):
    return_string = [f"{'{'}"]

    def inner(_dict, return_string, depth=0):
        for key in _dict.keys():
            if _dict[key]["type"] == "dict":
                depth += 2
                indient = TWO_INDIEND * (depth)
                return_string.append(f"{indient}{key}: {'{'}")
                value = _dict[key]['value']
                inner(value, return_string, depth)
                depth -= 2
                return_string.append(f"{indient}{'}'}")

            elif _dict[key]["type"] == "changed":
                indient = TWO_INDIEND * (depth + 1)
                value1 = to_string(changed_for_json(_dict[key]["value1"]),
                                   depth + 1)
                value2 = to_string(changed_for_json(_dict[key]["value2"]),
                                   depth + 1)
                return_string.append((f"{indient}- {key}: {value1}\n{indient}+ {key}: \
                                      {value2}"))

            else:
                type = _dict[key]["type"]
                indient = TWO_INDIEND * (depth + 1)
                value = to_string(changed_for_json(_dict[key]["value"]),
                                  depth + 1)
                return_string.append(f"{indient}{SIGN_TYPE[type]} {key}: \
                                    {value}")

        if depth == 0:
            return_string.append(f"{'}'}")
        return return_string
    return "\n".join(inner(_dict, return_string))
