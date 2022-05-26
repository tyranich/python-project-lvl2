import argparse
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
    parser = argparse.ArgumentParser(description='Compares two configuration files ans shows a difference.')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help='set format of output')
    args = parser.parse_args()

    
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
        return {x:val for x, val in dict_.items() if isinstance(val, dict)}
    
    def get_name(dict_):
        for _, _1 in dict_.items():
            return _
    def get_value(dict_):
        for _, _1 in dict_.items():
            return _1

    
    def stylish(pair_key=tuple, save_val=dict, dict_= dict, other=dict):
        if pair_key:
            key, val = pair_key[0].popitem()
            key1, val2 = pair_key[1].popitem()
            return_string = "- {}: {}\n+ {}: {}\n".format(key, val, key1, val2)
        elif save_val:
            key, val = save_val.popitem()
            return_string = "{}: {}\n".format(key, val)
        elif dict_:
            name = get_name(dict_)
            return_string = "{}: {"


    def testd(dict_, dict_2):
        sttring_return = []
        def hz(str_ , dict1, dict2):
            name_dict1 = get_name(dict1)
            not_changed = {} 
            deleted = {} 
            added = {}

            childs_1 = None
            childs_2 = None 
            for key, val in sorted(dict1.items()):
                if key in dict2.keys():
                    if isinstance(dict1[key], dict):
                        childs_1 = get_children(dict1[key])
                        childs_2 = get_children(dict2[key])
                        testd(childs_1, childs_2)
                    else:
                        if dict1[_] == dict2[_]:
                            not_changed = {key:val}
                        elif dict1[_] != dict2[_]:
                            deleted = {key:val}
                            added = {key:dict2[key]}
                else:
                    deleted = {key:val}

            return str_
        return hz(sttring_return, dict_, dict_2)
    


  
    
    file1, file2 = parser_data(args.first_file, args.second_file)
    a = testd(file1, file2)
    for _ in a:
       print(_)