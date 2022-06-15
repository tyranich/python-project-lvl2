from filecmp import dircmp
from logging.config import dictConfig
from tkinter import Y

def get_children(dict_):
    return {x:val for x, val in dict_.items()}

def get_name(dict_):
  for _, _1 in dict_.items():
      return _
def get_value(dict_):
  for _, _1 in dict_.items():
      return _1

a = {"group3": {'deep': {'id': {'number': 45}}, 'fee': 100500}}



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


def dict_string2(dict_, level):
        str_ = []
        def test_(dict1, level_, string_):
            name = get_name(dict1)
            childs = get_children(dict1)
            #string_.append("{}: {{\n".format(name))
            #level_ += 2
            for _ in childs:
                if isinstance(childs[_], dict):    
                    #string_.append(("  " * level_))
                    string_.append(("  " * level_)+_ + ": {\n")
                    level_ += 2
                    test_(childs[_], level_, string_)
                    level_ -= 2
                else:
                    string_.append(("  " * (level_)) + "{}: {}".format(_, childs[_]) + "\n")
            level_ -= 1
            string_.append("  " * (level_ + 1) + "}" + "\n")
            return string_
        return test_(dict_, level, str_)

b = {'group2': {'abc': 12345, 'deep': {'id': 45}}}
y = dict_string2(b, 0)
t = ""
for _ in y:
  t += _
print(t)