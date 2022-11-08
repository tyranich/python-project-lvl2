import argparse
from gendiff.scripts.parse_data import parser_data
from gendiff.scripts.formaters.stylish import stylish
from gendiff.scripts.formaters.plain import plain
import json


def get_children(dict_):
    return {x: val for x, val in dict_.items()}


def get_name(dict_):
    for _, _1 in dict_.items():
        return _


def get_value(dict_):
    for _, _1 in dict_.items():
        return _1


def is_changed(dict_return, sheet1=None, sheet2=None):

    if sheet1 and sheet2:
        if get_value(sheet1) == get_value(sheet2):
            dict_return[get_name(sheet1)] = {"status": "not changed",
                                             "value": get_value(sheet1)}
        elif get_value(sheet1) != get_value(sheet2):

            dict_return[get_name(sheet1)] = {"status": "changed",
                                             "value1": get_value(sheet1),
                                             "value2": get_value(sheet2)}


def generate_diff(dict1, dict2):
    file1, file2 = parser_data(dict1, dict2)
    dict_return = {}
    unification_val = set(file1) | set(file2)
    for sheet in sorted(unification_val):

        if sheet in file1.keys() and sheet in file2.keys():

            if isinstance(file1[sheet], dict) and \
                    isinstance(file2[sheet], dict):

                childs1 = get_children(file1[sheet])
                childs2 = get_children(file2[sheet])
                dict_return[sheet] = {"status": "dict", "value": {}}
                dict_return[sheet]["value"] = generate_diff(childs1, childs2)
            else:

                is_changed(dict_return, {sheet: file1[sheet]},
                           {sheet: file2[sheet]})

        elif sheet in file1.keys() and sheet not in file2.keys():

            dict_return[sheet] = {"status": "deleted", "value": file1[sheet]}
        elif sheet not in file1.keys() and sheet in file2.keys():

            dict_return[sheet] = {"status": "added", "value": file2[sheet]}
    return dict_return


def main():

    description = 'Compares two configuration files ans shows a difference.'
    parser = argparse.ArgumentParser(description)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", type=str,
                        default="stylish", help='set format of output')
    args = parser.parse_args()

    file1, file2 = parser_data(args.first_file, args.second_file)

    if args.format == "plain":
        done_dict = generate_diff(file1, file2)
        print("".join(plain(done_dict)))
    elif args.format == "json":
        done_dict = generate_diff(file1, file2)
        done_string = "".join(stylish(done_dict))
        data = json.dumps(done_string)
        print(data)
        data = json.loads(data)
        print(data)
    else:
        done_dict = generate_diff(file1, file2)
        print(done_dict)
        print("".join(stylish(done_dict)))


if __name__ == "__main__":
    main()
