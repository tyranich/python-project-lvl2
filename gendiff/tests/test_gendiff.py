from gendiff.gendiff import generate_diff
import pytest


path2 = "C:/Users/tyran/python-project-lvl2/second_file.json"
path1 = "C:/Users/tyran/python-project-lvl2/first_file.json"


def test_default():
    assert generate_diff(path1, path2) == '{\n- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n}'
    assert generate_diff(path2, path1) == '{\n+ follow: False\n  host: hexlet.io\n+ proxy: 123.234.53.22\n- timeout: 20\n+ timeout: 50\n- verbose: True\n}'

def test_empty_path():
    empty_path = ""
    with pytest.raises(FileNotFoundError):
        generate_diff(empty_path, path1)
        generate_diff(empty_path, empty_path)



print(test_default())