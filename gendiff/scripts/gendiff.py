import argparse
import os
from parse_data import parser_data, get_children
import copy 

def generate_diff(file1, file2):

    #file1, file2 = parser_data(path1, path2)
    if file1 and file2:
        pair_items = [x[0] for x in file1.items() if x in file2.items()]
        pair_keys = [x[0] for x in file1.items() if x[0] in file2.keys()]

        for _ in pair_items:
            pair_keys.remove(_)
        sorted_keys = sorted(set(file1).union(set(file2)))
        finished_list = []
        string_list = ["{"]
        for _2 in sorted_keys:
            if _2 in pair_items:
                finished_list.append((_2, file1.get(_2)))
            elif _2 in pair_keys:
                finished_list.append((_2, file1.get(_2), "-"))
                finished_list.append((_2, file2.get(_2), "+"))
            
            else:
                if file1.get(_2) != None:
                    finished_list.append((_2, file1.get(_2), "-"))
                elif file2.get(_2) != None:
                    finished_list.append((_2, file2.get(_2), "+"))

        for _3 in finished_list:
            if len(_3) == 3:
                concant_str = "{} {}: {}".format(_3[2], _3[0], _3[1])
            else:
                concant_str = "  {}: {}".format(_3[0], _3[1])
            string_list.append(concant_str)

        string_list.append("}")
        return ('\n'.join(string_list))
    else:
        return None


def stylish(first_file, second_file):

    name_dict_1 = get_name(first_file)
    name_dict_2 = get_name(second_file)

    childs_1 = get_children(first_file)
    childs_2 = get_children(second_file)
    
    pair_childs = {key:val for key, val in childs_1.items() if key in childs_2.keys()}



    



if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser(description='Compares two configuration files ans shows a difference.')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help='set format of output')
    args = parser.parse_args()
    """
    
    """
    file1, file2 = parser_data(args.first_file, args.second_file) #получаем содержимое файлов в виде словарей   
    pairs_keys = [x for x in file2.keys() if x in file1.keys()]
    childs_second = get_children(file2) #получаем список словарей, которые содержат ключ типа словарь
    child_first = get_children(file1) #получаем список словарей, которые содержат ключ типа словарь
    
    if pairs_keys:
        for i, _ in enumerate(pairs_keys):
            print(_)
            child_first_2 = get_children(child_first[i])
            print(pairs_keys)
            childs_second_2 = get_children(childs_second[i])
            print(child_first_2, "\n", childs_second_2)
    """
    def get_children(dict_):
        return {x:val for x, val in dict_.items()}
    
    def get_name(dict_):
        for _, _1 in dict_.items():
            return _
    def get_value(dict_):
        for _, _1 in dict_.items():
            return _1

    def dict_string(dict_):
        level = 0
        str_ = []
        def test_(dict1, level_, string_):
            name = get_name(dict1)
            val, childs = dict1.popitem()#get_children(dict1)
            string_.append("{}: {{\n".format(name))
            level_ += 1
            for _ in childs:
                if isinstance(childs[_], dict):    
                    string_.append(("    " * level_))
                    test_({_:childs[_]}, level_, string_)
                else:
                    string_.append(("    " * level_) + "{}: {}".format(_, childs[_]) + "\n")
            level_ -= 1
            string_.append("     " * level_ + "}" + "\n")
            return string_
        return test_(dict_, level, str_)

    def stylish(level_in, save_val=None, dict_= None, deleted = None, added = None, other=None, name = None):
        if added and deleted:
            key, val = deleted.popitem()
            key1, val2 = added.popitem()
            test_var = "  "  * level_in
            return_string = test_var + "- " + "{}: {}\n{}+ {}: {}\n".format(key, val, test_var, key1, val2)
        elif added:
            return_string = ""
            dict_added = None
            if dict_:
                dict_added = dict_string(added)
                return_string += "+ "
                for _ in dict_added:
                    return_string += _
            else:    
                key, val = added.popitem()
                return_string = "  "  * level_in + "+ "+"{}: {}\n".format(key, val)
        elif deleted:
            return_string = ""
            dict_deleted = None
            if dict_:
                dict_deleted = dict_string(deleted)
                return_string += "- "
                for _ in dict_deleted:
                    return_string += _
            else:
                key, val = deleted.popitem()
                return_string = "  "  * level_in + "- "+"{}: {}\n".format(key, val)
        elif save_val:
            key, val = save_val.popitem()
            return_string = "  "  * level_in + "{}: {}\n".format(key, val)
        elif dict_:
            key, val = dict_.popitem()
            if level_in == 1:
                return_string = "{}: {{\n".format(name)
            elif level_in > 1:
                return_string = "  " * level_in + "{}: {{\n".format(name)
        elif other:
            key, val = other.popitem()
            return_string = list(map(stylish(other=val)))
            return_string += "}"
        return return_string


    def testd(dict_, dict_2):
        sttring_return = []
        level = 0
        def hz(str_ , dict1, dict2, level_in):
            unification_val = set(dict1) | set(dict2)

            if dict1 == {} and dict2 == {}:
                return

            for _ in sorted(unification_val):
                if _ in dict1.keys() and _ in dict2.keys():
                    if isinstance(dict1[_], dict) and isinstance(dict2[_], dict):
                        level_in += 1 
                        childs_1 = get_children(dict1[_])
                        childs_2 = get_children(dict2[_])
                        str_.append(stylish(level_in, dict_= dict1[_], name=_))
                        hz(str_, childs_1, childs_2, level_in)
                        test_2 = "  " * level_in + "}\n"
                        str_.append(test_2)
                        level_in -= 1
                    elif dict1[_] == dict2[_]:
                        not_changed = {_:dict1[_]}
                        str_.append(stylish(level_in, save_val=not_changed))
                    elif dict1[_] != dict2[_]:
                            deleted = {_:dict1[_]}
                            added = {_:dict2[_]}
                            str_.append(stylish(level_in, deleted=deleted, added=added))

                elif _ in dict1.keys() and _ not in dict2.keys():
                    deleted = {_:dict1[_]}
                    if isinstance(dict1[_], dict):
                        str_.append(stylish(level_in, deleted=deleted, dict_=True))    
                    else:
                        str_.append(stylish(level_in, deleted=deleted))

                elif _ not in dict1.keys() and _ in dict2.keys():
                    added = {_:dict2[_]}
                    if isinstance(dict2[_], dict):
                        str_.append(stylish(level_in, added=added, dict_=True))
                    else:
                        str_.append(stylish(level_in, added=added))
                
            return str_
        return hz(sttring_return, dict_, dict_2, level)
    

    path = os.getcwd()
    path1 = path + "\\gendiff\\tests\\fixtures\\third_file.json" 
    path2 = path + "\\gendiff\\tests\\fixtures\\four_file.json"
    file1, file2 = parser_data(path1, path2)#(args.first_file, args.second_file)
    
    a = testd(file1, file2)
    f = ""
    for _ in a:
        f += _
    print(f)
    
    #for _ in a:
     #  print(_)