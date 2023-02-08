from gendiff.parse_data import open_data
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json_formater
from gendiff.create_tree_diff import build_tree_diff
from gendiff.open_file import open_file


def choising_formater(formater):

    if formater == "stylish":
        return stylish
    elif formater == "plain":
        return plain
    elif formater == "json":
        return json_formater


def generate_diff(path1, path2, formater='stylish'):  # noqa: C901

    formater = choising_formater(formater)
    data1, type_file = open_file(path1)
    dict1 = open_data(data1, type_file)
    data2, type_file = open_file(path2)
    dict2 = open_data(data2, type_file)
    return formater(build_tree_diff(dict1, dict2))
