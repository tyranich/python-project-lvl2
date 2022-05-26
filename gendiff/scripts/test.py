test = {
    "common": {
      "setting1": "Value 1",
      "setting2": 200,
      "setting3": True,
      "setting6": {
        "key": "value",
        "doge": {
          "wow": ""
        }
      }
    },
    "group1": {
      "baz": "bas",
      "foo": "bar",
      "nest": {
        "key": "value"
      }
    },
    "group2": 3#{
      #"abc": 12345,
      #"deep": {
        #"id": 45
      #}
    #}
  }
  
def get_children(dict_):
    return {x:val for x, val in dict_.items() if isinstance(val, dict)}
    
a = get_children(test)

def testd(dict_, dict_2):
    
    childs = get_children(dict_)
    childs_2 = get_children(dict_2)
    pairs_keys = set(childs) & set(childs_2)
    not_pairs_keys = set(childs) ^ set(childs_2)
    
    if childs == {}:
        return 
    print(childs)
    
    #sorted_child = filter(lambda x: if x in pair_keys, child)
    return_list = list(map(
        lambda child: testd(childs[child]), childs))
    #if return_list == None:
    #    return return_list
    
    return return_list
a = testd(test)
print(a)
    
    