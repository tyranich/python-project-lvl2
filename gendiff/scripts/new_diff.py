import os
from traceback import print_tb
from parse_data import parser_data
import json

def get_children(dict_):
    return {x:val for x, val in dict_.items()}

def get_name(dict_):
    for _, _1 in dict_.items():
        return _
def get_value(dict_):
    for _, _1 in dict_.items():
        return _1

def new_diff(dict1, dict2):
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
        return dict_
    
    return inside_func(dict_return, dict1, dict2)
 
def dict_string(dict_, level):
        str_ = []
        def test_(dict1, level_, string_):
            name = get_name(dict1)
            childs = get_children(dict1)
            level_ += 2
            for _ in childs:
                if isinstance(childs[_], dict):    
                    string_.append(("  " * level_)+_ + ": {\n")
                    test_(childs[_], level_, string_)
                else:
                    string_.append(("  " * (level_)) + "{}: {}".format(_, childs[_]) + "\n")
            level_ -= 1
            string_.append("  " * (level_ - 1) + "}\n")
            return string_
        return test_(dict_, level, str_)

def stylish(_dict):
    return_str = []
    level = 0
    def create_str(return_str, level, _dict, key=None):
        tabs_two = "  "
        for _ in _dict.keys():
            f = _
            if _dict[_]["status"] == "dict":
                return_str.append( "{}{}: {{\n".format(tabs_two * (level + 2), _, _dict[_]))
                create_str(return_str, level + 2, _dict[_]['value'])
                return_str.append("{}}}\n".format(tabs_two * (level + 2)))
            elif _dict[_]["status"] == "added":
                if isinstance(_dict[_]["value"], dict):
                    return_str.append( "{}+ {}: {{\n".format(tabs_two * (level + 1), _,))
                    с = "".join(dict_string(_dict[_]["value"], level + 2))
                    return_str.append("{}".format(с))
                else:    
                    return_str.append("{}+ {}: {}\n".format(tabs_two * (level + 1), _, _dict[_]["value"]))
            elif _dict[_]["status"] == "deleted":
                if isinstance(_dict[_]["value"], dict):
                    return_str.append( "{}- {}: {{\n".format(tabs_two * (level + 1), _,))
                    с = "".join(dict_string(_dict[_]["value"], level + 2))
                    return_str.append("{}".format(с))
                else:
                    return_str.append( "{}- {}: {}\n".format(tabs_two * (level + 1), _, _dict[_]["value"]))
            elif _dict[_]["status"] == "changed":
                if isinstance(_dict[_]["value1"], dict):
                    return_str.append( "{}- {}: {{\n".format(tabs_two * (level + 1), _,))
                    с = "".join(dict_string(_dict[_]["value1"], level + 2))
                    return_str.append("{}".format(с))
                else:
                    return_str.append( "{}- {}: {}\n".format(tabs_two * (level + 1), _, _dict[_]["value1"]))

                if  isinstance(_dict[_]["value2"], dict):
                    return_str.append( "{}+ {}: {{\n".format(tabs_two * (level + 1), _,))
                    с = "".join(dict_string(_dict[_]["value2"], level + 2))
                    return_str.append("{}".format(с))
                else:
                    return_str.append( "{}+ {}: {}\n".format(tabs_two * (level + 1), _, _dict[_]["value2"]))
            elif _dict[_]["status"] == "not changed":
                return_str.append( "{}{}: {}\n".format(tabs_two * (level + 2), _, _dict[_]["value"]))
        
        return return_str
    return create_str(return_str, level, _dict)

def plain(_dict):
    return_str = []
    level = 0
    def create_str(return_str, level, _dict, name):
        tabs_two = "  "
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
                    if isinstance(_dict[_]["value"], dict) or isinstance(_dict[_]["value"], list):
                        value = ["complex value"]
                        print("Property '{}' was added with value: {}".format(_, value))
                    else:
                        print("Property '{}' was added with value: {}".format(_, value))
                else:    
                    if isinstance(_dict[_]["value"], dict) or isinstance(_dict[_]["value"], list):
                        value = ["complex value"]
                        print("Property '{}.{}' was added with value: {}".format(name, _, value))
                    else:
                        print("Property '{}.{}' was added with value: {}".format(name, _, value))

            elif _dict[_]["status"] == "deleted":
                if level == 0:
                    print("Property '{}' was removed".format(_))
                else: 
                    print("Property '{}.{}' was removed".format(name, _))
                

            elif _dict[_]["status"] == "changed":
                value1 = _dict[_]["value1"]
                value2 = _dict[_]["value2"]
                if isinstance(_dict[_]["value1"], dict) or isinstance(_dict[_]["value1"], list):
                    value1 = '[comlex value]'
                if isinstance(_dict[_]["value2"], dict) or isinstance(_dict[_]["value2"], list):
                    value2 = '[complex value]'
                print("Property '{}.{}' was update. From {} to {}".format(name,_,value1,value2))
        return return_str
    return create_str(return_str, level, _dict, "")

path = os.getcwd()
path1 = path + "\\gendiff\\tests\\fixtures\\third_file.json" 
path2 = path + "\\gendiff\\tests\\fixtures\\four_file.json"
file1, file2 = parser_data(path1, path2)#(args.first_file, args.second_file)

a = new_diff(file1, file2)
print(a)
c = plain(a)#stylish_test(a)
#g = ""
#for _ in c:
#    for _1 in _:
#        g += _1
#data = json.dumps(g)  
#data = json.loads(data)
#print(g)