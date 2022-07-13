import pytest
from gendiff.scripts.formaters.stylish import stylish
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parse_data import parser_data

path_json_2 = ("C:/Users/tyran/python-project-lvl2/gendiff/"
               "tests/fixtures/second_file.json")
path_json = ("C:/Users/tyran/python-project-lvl2/"
             "gendiff/tests/fixtures/first_file.json")

path_yml_2 = ("C:/Users/tyran/python-project-lvl2/"
              "gendiff/tests/fixtures/second_file.yml")
path_yml = ("C:/Users/tyran/python-project-lvl2/"
            "gendiff/tests/fixtures/first_file.yml")
file_json, file_json2 = parser_data(path_json, path_json_2)
file_yml, file_yml2 = parser_data(path_yml, path_yml_2)

def test_default():
    done_dict = generate_diff(file_json, file_json2)
    a = "".join(stylish(done_dict))
    assert a == ("{\n- follow: False\n"
                 "  host: hexlet.io\n"
                 "- proxy: 123.234.53.22\n"
                 "- timeout: 50\n"
                 "+ timeout: 20\n"
                 "+ verbose: True\n}")
    done_dict = generate_diff(file_json2, file_json)
    assert "".join(stylish(done_dict)) == ("{\n+ follow: False\n"
                                           "  host: hexlet.io\n"
                                           "+ proxy: 123.234.53.22\n"
                                           "- timeout: 20\n"
                                           "+ timeout: 50\n"
                                           "- verbose: True\n}")
    
    done_dict = generate_diff(file_yml, file_yml2)
    assert "".join(stylish(done_dict)) == ("{\n- follow: False\n"
                                           "  host: hexlet.io\n"
                                           "- proxy: 123.234.53.22\n"
                                           "- timeout: 50\n"
                                           "+ timeout: 20\n"
                                           "+ verbose: True\n}")
    done_dict = generate_diff(file_yml2, file_yml)
    assert "".join(stylish(done_dict)) == ("{\n+ follow: False\n"
                                           "  host: hexlet.io\n"
                                           "+ proxy: 123.234.53.22\n"
                                           "- timeout: 20\n"
                                           "+ timeout: 50\n"
                                           "- verbose: True\n}")


def test_empty_path():
    empty_path = ""
    assert generate_diff(empty_path, path_json) is None
    assert generate_diff(empty_path, empty_path) is None


print(test_default())
