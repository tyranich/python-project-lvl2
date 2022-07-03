import argparse
from parse_data import parser_data
from formaters.stylish import stylish
from formaters.plain import plain


def get_children(dict_):
    return {x: val for x, val in dict_.items()}


def get_name(dict_):
    for _, _1 in dict_.items():
        return _


def get_value(dict_):
    for _, _1 in dict_.items():
        return _1


def generate_diff(dict1, dict2, format_name=stylish):
    dict_return = {}

    def inside_func(dict_, dict1, dict2):

        unification_val = set(dict1) | set(dict2)
        #if dict1 == {} and dict2 == {}:
            #return
        for sheet in sorted(unification_val):
            if sheet in dict1.keys() and sheet in dict2.keys():

                if isinstance(dict1[sheet], dict) and \
                        isinstance(dict2[sheet], dict):

                    childs1 = get_children(dict1[sheet])
                    childs2 = get_children(dict2[sheet])
                    dict_[sheet] = {"status": "dict", "value": {}}
                    inside_func(dict_[sheet]["value"], childs1, childs2)
                elif dict1[sheet] == dict2[sheet]:

                    dict_[sheet] = {"status": "not changed",
                                    "value": dict1[sheet]}
                elif dict1[sheet] != dict2[sheet]:

                    dict_[sheet] = {"status": "changed", "value1": dict1[sheet],
                                    "value2": dict2[sheet]}

            elif sheet in dict1.keys() and sheet not in dict2.keys():

                dict_[sheet] = {"status": "deleted", "value": dict1[sheet]}
            elif sheet not in dict1.keys() and sheet in dict2.keys():

                dict_[sheet] = {"status": "added", "value": dict2[sheet]}
        return "".join(format_name(dict_))

    return inside_func(dict_return, dict1, dict2)


if __name__ == "__main__":

    description = 'Compares two configuration files ans shows a difference.'
    parser = argparse.ArgumentParser(description)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", type=str,
                        default="stylish", help='set format of output')
    args = parser.parse_args()

    file1, file2 = parser_data(args.first_file, args.second_file)

    if args.format == "plain":
        print(generate_diff(file1, file2, plain))
    else:
        print(generate_diff(file1, file2))
