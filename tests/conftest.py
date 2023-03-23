import os
import pytest

FOLDER_FIXTURE = 'fixtures'


@pytest.fixture(scope='session')
def file1_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file1.json')


@pytest.fixture(scope='session')
def file2_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file2.json')


@pytest.fixture(scope='session')
def file1_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file1.yml')


@pytest.fixture(scope='session')
def file2_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file2.yaml')


@pytest.fixture(scope='session')
def file1_tree_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file1tree.json')


@pytest.fixture(scope='session')
def file2_tree_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file2tree.json')


@pytest.fixture(scope='session')
def file1_tree_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file1tree.yml')


@pytest.fixture(scope='session')
def file2_tree_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file2tree.yaml')


@pytest.fixture(scope='session')
def result_jsontree():
    result_path = os.path.join(os.path.dirname(__file__),
                               FOLDER_FIXTURE,
                               'jsontree')
    with open(result_path) as file:
        return file.read()


@pytest.fixture(scope='session')
def result_plaintree():
    result_path = os.path.join(os.path.dirname(__file__),
                               FOLDER_FIXTURE,
                               'plaintree')
    with open(result_path) as file:
        return file.read()


@pytest.fixture(scope='session')
def result_stylishplane():
    result_path = os.path.join(os.path.dirname(__file__),
                               FOLDER_FIXTURE,
                               'stylishplane')
    with open(result_path) as file:
        return file.read()


@pytest.fixture(scope='session')
def result_stylishtree():
    result_path = os.path.join(os.path.dirname(__file__),
                               FOLDER_FIXTURE,
                               'stylishtree')

    with open(result_path) as file:
        return file.read()


@pytest.fixture(scope='session')
def formater_stylish():
    return "stylish"


@pytest.fixture(scope='session')
def formater_plain():
    return "plain"


@pytest.fixture(scope='session')
def formater_json():
    return "json"
