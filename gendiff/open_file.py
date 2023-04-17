
def open_file(path):

    if path.endswith('.yaml') or path.endswith('.yml'):
        with open(path) as file:
            return_data = file.read()
        return (return_data, 'yml')

    elif path.endswith('.json'):
        with open(path) as file:
            return_data = file.read()
            return (return_data, 'json')
