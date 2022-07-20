def get_value(dict_):
    return dict_['value']


def if_added(level, dict_, root, name):
    value = dict_[name]["value"]
    if level == 0:

        if isinstance(dict_[name]["value"], dict) or \
                isinstance(dict_[name]["value"], list):
            value = ["complex value"]
            print("Property '{}' was added with value: {}"
                  .format(name, value))
        else:
            print("Property '{}' was added with value: {}"
                  .format(name, value))
    else:
        if isinstance(dict_[name]["value"], dict) or \
                isinstance(dict_[name]["value"], list):
            value = ["complex value"]
            print("Property '{}.{}' was added with value: {}".
                  format(root, name, value))
        else:
            print("Property '{}.{}' was added with value: {}".
                  format(root, name, value))


def if_deleted(level, root, name):
    if level == 0:
        print("Property '{}' was removed".format(name))
    else:
        print("Property '{}.{}' was removed".format(root, name))


def if_changed(level, dict_, root, name):
    value1 = dict_[name]["value1"]
    value2 = dict_[name]["value2"]
    if isinstance(dict_[name]["value1"], dict) or \
            isinstance(dict_[name]["value1"], list):
        value1 = '[comlex value]'
    if isinstance(dict_[name]["value2"], dict) or \
            isinstance(dict_[name]["value2"], list):
        value2 = '[complex value]'
    print("Property '{}.{}' was update. From {} to {}".
          format(root, name, value1, value2))


def choise_status(dict_status, level, dict_, root, name):

    if dict_status == "added":
        if_added(level, dict_, root, name)
    elif dict_status == "deleted":
        if_deleted(level, root, name)
    elif dict_status == "changed":
        if_changed(level, dict_, root, name)


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
            else:

                choise_status(_dict[_]["status"], level, _dict, name, _)

        return return_str
    return create_str(return_str, level, _dict, "")
