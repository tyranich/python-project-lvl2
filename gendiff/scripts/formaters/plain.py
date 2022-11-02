from getters import changed_for_json, get_value


def if_added(level, dict_, root, name):
    value = get_value(dict_[name])#["value"] 
    if level == 0:
        #if isinstance(dict_[name]["value"], dict) or \
        if isinstance(get_value(dict_[name]), dict) or \
                isinstance(get_value(dict_[name]), list): #isinstance(dict_[name]["value"], list):
            value = ["complex value"]
            print("Property '{}' was added with value: {}"
                  .format(name, value))
        else:
            print("Property '{}' was added with value: {}"
                  .format(name, value))
    else:
        #if isinstance(dict_[name]["value"], dict) or \
        if isinstance(get_value(dict_[name]), dict) or \
                isinstance(get_value(dict_[name]), list):#isinstance(dict_[name]["value"], list):
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
    value1 = changed_for_json(dict_[name]["value1"])
    value2 = changed_for_json(dict_[name]["value2"])
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

        for key in _dict.keys():

            if _dict[key]["status"] == "dict":
                if level == 0:
                    name2 = key
                else:
                    name2 = f"{name}.{key}"
                level += 1
                create_str(return_str, level + 2, get_value(_dict[key]), name2) #['value']
                level -= 1
            else:

                choise_status(_dict[key]["status"], level, _dict, name, key)

        return return_str
    return create_str(return_str, level, _dict, "")
