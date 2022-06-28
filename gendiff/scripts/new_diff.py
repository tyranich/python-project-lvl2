import os
from parse_data import parser_data
from formaters.stylish import stylish
def get_children(dict_):
    return {x:val for x, val in dict_.items()}

def get_name(dict_):
    for _, _1 in dict_.items():
        return _
def get_value(dict_):
    for _, _1 in dict_.items():
        return _1


    
def inside_func(dict1, dict2):
    dict_return = {}
    unification_val = set(dict1) | set(dict2)
    if dict1 == {} and dict2 == {}:
            return
    for _ in sorted(unification_val):
        if _ in dict1.keys() and _ in dict2.keys():
            if isinstance(dict1[_], dict) and isinstance(dict2[_], dict):
                childs1 = get_children(dict1[_])
                childs2 = get_children(dict2[_])
                dict_return[_] = {"status": "dict", "value":{}}
                dict_return[_]["value"] = inside_func(childs1, childs2)
            elif dict1[_] == dict2[_]:
                dict_return[_] = {"status":"not changed", "value":dict1[_]}
            elif dict1[_] != dict2[_]:
                dict_return[_] = {"status":"changed", "value1":dict1[_], "value2":dict2[_]}
        
        elif _ in dict1.keys() and _ not in dict2.keys():
                if isinstance(dict1[_], dict):
                    dict_return[_] = {"status": "deleted", "value": dict1[_]}
                else:
                    dict_return[_] = {"status": "deleted", "value":dict1[_]}

        elif _ not in dict1.keys() and _ in dict2.keys():
            if isinstance(dict2[_], dict):
                dict_return[_] = {"status": "added", "value": dict2[_]}
            else:
                dict_return[_] = {"status": "added", "value": dict2[_]}
    return dict_return


 
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



path = os.getcwd()
path1 = path + "\\gendiff\\tests\\fixtures\\third_file.json" 
path2 = path + "\\gendiff\\tests\\fixtures\\four_file.json"
file1, file2 = parser_data(path1, path2)#(args.first_file, args.second_file)

a = generate_diff(file1, file2)
print(a)
#print("".join(stylish(a)))
#g = ""
#for _ in c:
#    for _1 in _:
#        g += _1
#data = json.dumps(g)  
#data = json.loads(data)
#print(g)