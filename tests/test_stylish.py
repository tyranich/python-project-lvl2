from gendiff import generate_diff


FORMATTER = 'stylish'
FILEMODE = 'tree'


def test_json(file1_tree_json_path, file2_tree_json_path, result_render):
    assert result_render == generate_diff(file1_tree_json_path,
                                          file2_tree_json_path,
                                          formater=FORMATTER)


def test_yml(file1_tree_yml_path, file2_tree_yml_path, result_render):
    assert result_render == generate_diff(file1_tree_yml_path,
                                          file2_tree_yml_path,
                                          formater=FORMATTER)