import json
import yaml


def parser_data(path1, path2):
    
    if path1 and path2:
        if path1.endswith('.yaml') or path1.endswith('.yml'):
            if path2.endswith('.yaml') or path2.endswith('.yml'):
                file1 = yaml.load(open(path1), yaml.SafeLoader)
                file2 = yaml.load(open(path2), yaml.SafeLoader)
        
        if path1.endswith('.json') and path2.endswith('.json'):
            file1 = json.load(open(path1))
            file2 = json.load(open(path2))
        
        return file1, file2
    
    else:
        return None, None