import pytest
from main_task_2 import create_folder, del_folder


@pytest.mark.parametrize('name_folder, stat_code', [('Some_folder', 200), ('1234', 200)])
def test_create_folder(name_folder, stat_code):
    assert create_folder(name_folder).status_code == stat_code
    assert type(name_folder) == str
    del_folder(name_folder)


@pytest.mark.parametrize('name_folder,  error',
                         [([1223], AssertionError,), (1234, AssertionError,)])
def test_create_folder_typeerror(name_folder, error):
    with pytest.raises(error):
        assert type(name_folder) == str
    del_folder(name_folder)


@pytest.mark.parametrize('name_folder, stat_code, error',
                         [('Some_folder', 100, AssertionError,), ('1234', 500, AssertionError,)])
def test_create_folder_errorresp(name_folder, stat_code, error):
    with pytest.raises(error):
        assert create_folder(name_folder).status_code == stat_code
    del_folder(name_folder)