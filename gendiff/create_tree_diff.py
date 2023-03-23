
def build_tree_diff(dict1, dict2):

    dict_return = {}
    unification_val = set(dict1) | set(dict2)
    for sheet in sorted(unification_val):

        if isinstance(dict1.get(sheet), dict) and \
                isinstance(dict2.get(sheet), dict):

            dict_return[sheet] = {"type": "dict", "value": {}}
            dict_return[sheet]["value"] = build_tree_diff(dict1[sheet],
                                                          dict2[sheet])

        elif dict1.get(sheet) == dict2.get(sheet):
            dict_return[sheet] = {"type": "not changed",
                                  "value": dict1[sheet]}

        elif sheet not in dict2.keys():
            dict_return[sheet] = {"type": "deleted",
                                  "value": dict1[sheet]}

        elif sheet not in dict1.keys():
            dict_return[sheet] = {"type": "added",
                                  "value": dict2[sheet]}

        else:
            dict_return[sheet] = {"type": "changed",
                                  "value1": dict1[sheet],
                                  "value2": dict2[sheet]}
    print(dict_return)
    return dict_return
