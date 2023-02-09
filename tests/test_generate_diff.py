from gendiff import generate_diff
import pytest

FORMATTER = 'plain'
FILEMODE = 'tree'


# test plain
@pytest.mark.parametrize("file1, file2, result",
                         [
                            pytest.lazy_fixture(('file1_tree_json_path',
                            'file2_tree_json_path', 'result_render')),
                            pytest.lazy_fixture(('file1_tree_yml_path',
                            'file2_tree_yml_path', 'result_render'))
                         ])
def tests_plain(file1, file2, result):
    assert result == generate_diff(file1, file2, formater=FORMATTER)


# test json
FORMATTER='json'


@pytest.mark.parametrize("file1, file2, result",
                         [
                            pytest.lazy_fixture(('file1_tree_json_path',
                            'file2_tree_json_path', 'result_render')),
                            pytest.lazy_fixture(('file1_tree_yml_path',
                            'file2_tree_yml_path', 'result_render'))
                         ])
def tests_json(file1, file2, result):
    assert result == generate_diff(file1, file2, formater=FORMATTER)


# test stylish
FORMATTER='stylish'


@pytest.mark.parametrize("file1, file2, result",
                         [
                            pytest.lazy_fixture(('file1_tree_json_path',
                            'file2_tree_json_path', 'result_render')),
                            pytest.lazy_fixture(('file1_tree_yml_path',
                            'file2_tree_yml_path', 'result_render'))
                         ])
def tests_stylish(file1, file2, result):
    assert result == generate_diff(file1, file2, formater=FORMATTER)
