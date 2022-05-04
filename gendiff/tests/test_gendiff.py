from importlib.resources import path
from gendiff.scripts.gendiff import generate_diff
import pytest


path_json_2 = "C:/Users/tyran/python-project-lvl2/gendiff/tests/fixtures/second_file.json"
path_json = "C:/Users/tyran/python-project-lvl2/gendiff/tests/fixtures/first_file.json"

path_yml_2 = "C:/Users/tyran/python-project-lvl2/gendiff/tests/fixtures/second_file.yml"
path_yml = "C:/Users/tyran/python-project-lvl2/gendiff/tests/fixtures/first_file.yml"

def test_default():
    #test json files
    assert generate_diff(path_json, path_json_2) == '{\n- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n}'
    assert generate_diff(path_json_2, path_json) == '{\n+ follow: False\n  host: hexlet.io\n+ proxy: 123.234.53.22\n- timeout: 20\n+ timeout: 50\n- verbose: True\n}'
    #test yml files
    assert generate_diff(path_yml, path_yml_2) == '{\n- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n}'
    assert generate_diff(path_yml_2, path_yml) == '{\n+ follow: False\n  host: hexlet.io\n+ proxy: 123.234.53.22\n- timeout: 20\n+ timeout: 50\n- verbose: True\n}'
    
def test_empty_path():
    empty_path = ""
    assert generate_diff(empty_path, path_json) == None
    assert generate_diff(empty_path, empty_path) == None



print(test_default())