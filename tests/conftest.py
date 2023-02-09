import os
import pytest

FOLDER_FIXTURE = 'fixtures'


# plain file1 for test
@pytest.fixture(scope='session')
def file1_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file1.json')


# plain file2 for test
@pytest.fixture(scope='session')
def file2_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file2.json')


# plain file1 for test
@pytest.fixture(scope='session')
def file1_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file1.yml')


# plain file2 for test
@pytest.fixture(scope='session')
def file2_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file2.yaml')


# nested file1 for test
@pytest.fixture(scope='session')
def file1_tree_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file1tree.json')


# nested file2 for test
@pytest.fixture(scope='session')
def file2_tree_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file2tree.json')


# nested file1 for test
@pytest.fixture(scope='session')
def file1_tree_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file1tree.yml')


# nested file2 for test
@pytest.fixture(scope='session')
def file2_tree_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FOLDER_FIXTURE,
                        'file2tree.yaml')


@pytest.fixture(scope='function')
def result_render(request):
    assert getattr(request.module, 'FORMATTER', None)
    result_path = os.path.join(os.path.dirname(__file__),
                               FOLDER_FIXTURE,
                               request.module.FORMATTER
                               + request.module.FILEMODE)
    with open(result_path) as file:
        return file.read()
