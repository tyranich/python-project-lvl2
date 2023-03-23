from gendiff.parse_data import parse_data
from gendiff.formaters.stylish import stylish  # noqa: F401
from gendiff.formaters.plain import plain  # noqa: F401
from gendiff.formaters.json import json_formater  # noqa: F401
from gendiff.create_tree_diff import build_tree_diff
from gendiff.open_file import open_file
from gendiff.formaters.choise_formater import choising_formater


def generate_diff(path1, path2, formater='stylish'):  # noqa: C901

    formater = choising_formater(formater)
    data1, type_file = open_file(path1)
    dict1 = parse_data(data1, type_file)
    data2, type_file = open_file(path2)
    dict2 = parse_data(data2, type_file)
    return formater(build_tree_diff(dict1, dict2))
