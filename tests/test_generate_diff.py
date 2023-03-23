from gendiff import generate_diff
import pytest


FILES_FOR_TESTS_1 = ('file1_tree_json_path', 'file2_tree_json_path',
                     "formater_stylish", 'result_stylishtree')


FILES_FOR_TESTS_2 = ('file1_tree_json_path', 'file2_tree_json_path',
                     "formater_plain", 'result_plaintree')


FILES_FOR_TESTS_3 = ('file1_tree_json_path', 'file2_tree_json_path',
                     "formater_json", 'result_jsontree')


FILES_FOR_TESTS_4 = ('file1_tree_yml_path', 'file2_tree_yml_path',
                     "formater_stylish", 'result_stylishtree')


FILES_FOR_TESTS_5 = ('file1_tree_yml_path', 'file2_tree_yml_path',
                     "formater_plain", 'result_plaintree')


FILES_FOR_TESTS_6 = ('file1_tree_yml_path', 'file2_tree_yml_path',
                     "formater_json", 'result_jsontree')


@pytest.mark.parametrize("file1, file2, formater, result",
                         [pytest.lazy_fixture(FILES_FOR_TESTS_1),
                          pytest.lazy_fixture(FILES_FOR_TESTS_2),
                          pytest.lazy_fixture(FILES_FOR_TESTS_3),
                          pytest.lazy_fixture(FILES_FOR_TESTS_4),
                          pytest.lazy_fixture(FILES_FOR_TESTS_5),
                          pytest.lazy_fixture(FILES_FOR_TESTS_6),
                          ])
def tests_all(file1, file2, formater, result):
    assert result == generate_diff(file1, file2, formater=formater)
