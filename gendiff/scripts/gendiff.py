import argparse
from parse_data import parser_data
from formaters.stylish import stylish
from formaters.plain import plain


def get_children(dict_):
    return {x:val for x, val in dict_.items()}


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
        if dict1 == {} and dict2 == {}:
                return
        for _ in sorted(unification_val):
            if _ in dict1.keys() and _ in dict2.keys():
                if isinstance(dict1[_], dict) and isinstance(dict2[_], dict):
                    childs1 = get_children(dict1[_])
                    childs2 = get_children(dict2[_])
                    dict_[_] = {"status": "dict", "value":{}}
                    inside_func(dict_[_]["value"], childs1, childs2)
                elif dict1[_] == dict2[_]:
                    dict_[_] = {"status":"not changed", "value":dict1[_]}
                elif dict1[_] != dict2[_]:
                    dict_[_] = {"status":"changed", "value1":dict1[_], "value2":dict2[_]}
            
            elif _ in dict1.keys() and _ not in dict2.keys():
                    if isinstance(dict1[_], dict):
                        dict_[_] = {"status": "deleted", "value": dict1[_]}
                    else:
                        dict_[_] = {"status": "deleted", "value":dict1[_]}

            elif _ not in dict1.keys() and _ in dict2.keys():
                if isinstance(dict2[_], dict):
                    dict_[_] = {"status": "added", "value": dict2[_]}
                else:
                    dict_[_] = {"status": "added", "value": dict2[_]}
        return "".join(format_name(dict_))
    
    return inside_func(dict_return, dict1, dict2)
 

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Compares two configuration files ans shows a difference.')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help='set format of output')
    args = parser.parse_args()
    
    file1, file2 = parser_data(args.first_file, args.second_file) #получаем содержимое файлов в виде словарей   
    print(generate_diff(file1, file2))
    
    """
    path_to_root = os.getcwd()
    path1 = path_to_root + f"\\gendiff\\tests\\fixtures\\args.first_file}" 
    path2 = path_to_root + f"\\gendiff\\tests\\fixtures\\{args.second_file}"
    file1, file2 = parser_data(path1, path2)#(args.first_file, args.second_file)
    """
