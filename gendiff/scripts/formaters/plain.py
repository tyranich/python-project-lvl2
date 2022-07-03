def get_value(dict_):
    return dict_['value']


def plain(_dict):
    return_str = []
    level = 0

    def create_str(return_str, level, _dict, name):

        for _ in _dict.keys():
            if _dict[_]["status"] == "dict":
                if level == 0:
                    name2 = _
                else:
                    name2 = f"{name}.{_}"
                level += 1
                create_str(return_str, level + 2, _dict[_]['value'], name2)
                level -= 1
            elif _dict[_]["status"] == "added":
                value = _dict[_]["value"]
                if level == 0:

                    if isinstance(_dict[_]["value"], dict) or \
                            isinstance(_dict[_]["value"], list):
                        value = ["complex value"]
                        print("Property '{}' was added with value: {}"
                              .format(_, value))
                    else:
                        print("Property '{}' was added with value: {}"
                              .format(_, value))
                else:
                    if isinstance(_dict[_]["value"], dict) or \
                            isinstance(_dict[_]["value"], list):
                        value = ["complex value"]
                        print("Property '{}.{}' was added with value: {}".
                              format(name, _, value))
                    else:
                        print("Property '{}.{}' was added with value: {}".
                              format(name, _, value))

            elif _dict[_]["status"] == "deleted":
                if level == 0:
                    print("Property '{}' was removed".format(_))
                else:
                    print("Property '{}.{}' was removed".format(name, _))

            elif _dict[_]["status"] == "changed":
                value1 = _dict[_]["value1"]
                value2 = _dict[_]["value2"]
                if isinstance(_dict[_]["value1"], dict) or \
                        isinstance(_dict[_]["value1"], list):
                    value1 = '[comlex value]'
                if isinstance(_dict[_]["value2"], dict) or \
                        isinstance(_dict[_]["value2"], list):
                    value2 = '[complex value]'
                print("Property '{}.{}' was update. From {} to {}".
                      format(name, _, value1, value2))
        return return_str
    return create_str(return_str, level, _dict, "")
