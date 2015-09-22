import test.utils

__author__ = 'thauser'
from mock import MagicMock, patch
from pnc_cli import environments


@patch('pnc_cli.environments._environment_exists', return_value=True)
def test_get_environment_id_id(mock):
    result = environments.get_environment_id(1, None)
    mock.assert_called_once_with(1)
    assert result == 1

@patch('pnc_cli.environments._environment_exists', return_value=False)
def test_get_environment_id_notexist(mock):
    result = environments.get_environment_id(1, None)
    mock.assert_called_once_with(1)
    assert not result

@patch('pnc_cli.environments._get_environment_id_by_name', return_value=1)
def test_get_environment_id_name(mock):
    result = environments.get_environment_id(None, 'testerino')
    mock.assert_called_once_with('testerino')
    assert result == 1

@patch('pnc_cli.environments._get_environment_id_by_name', return_value=None)
def test_get_environment_id_name_notexist(mock):
    result = environments.get_environment_id(None, 'testerino')
    mock.assert_called_once_with('testerino')
    assert not result

def test_get_environment_id_none():
    result = environments.get_environment_id(None, None)
    assert not result

@patch('pnc_cli.environments.envs_api.get_all', return_value=MagicMock(content=[MagicMock(id=1)]))
def test_environment_exists(mock):
    result = environments._environment_exists(1)
    mock.assert_called_once_with()
    assert result

@patch('pnc_cli.environments.envs_api.get_all', return_value=MagicMock(content=[MagicMock(id=1)]))
def test_environment_exists_false(mock):
    result = environments._environment_exists(2)
    mock.assert_called_once_with()
    assert not result

@patch('pnc_cli.environments.envs_api.get_all')
def test_get_environment_id_by_name(mock):
    mock.return_value = test.utils.create_mock_list_with_name_attribute()
    result = environments._get_environment_id_by_name('testerino')
    mock.assert_called_once_with()
    assert result == 1

@patch('pnc_cli.environments.envs_api.get_all')
def test_get_environment_id_by_name_notexist(mock):
    mock.return_value = test.utils.create_mock_list_with_name_attribute()
    result = environments._get_environment_id_by_name('doesntexist')
    mock.assert_called_once_with()
    assert not result

@patch('pnc_cli.environments._create_environment_object', return_value='test-environment-object')
@patch('pnc_cli.environments.envs_api.create_new', return_value=MagicMock(content='buildenvironment1'))
def test_create_environment(mock_create_new, mock_create_environment_object):
    result = environments.create_environment(name='testerino',build_type='JAVA')
    mock_create_environment_object.assert_called_once_with(name='testerino', build_type='JAVA')
    mock_create_new.assert_called_once_with(body='test-environment-object')
    assert result == 'buildenvironment1'


@patch('pnc_cli.environments._environment_exists', return_value=1)
@patch('pnc_cli.environments.envs_api.get_specific', return_value=MagicMock(content=environments._create_environment_object(name='testerino', build_type='JAVA')))
@patch('pnc_cli.environments.envs_api.update', return_value=MagicMock(content='buildenvironment1'))
def test_update_environment(mock_update, mock_get_specific, mock_environment_exists):
    result = environments.update_environment(id=1, name='testerino2', build_type='JAVA')
    mock_environment_exists.assert_called_once_with(1)
    mock_get_specific.assert_called_once_with(id=1)
    kwargs = mock_update.call_args
    env = environments._create_environment_object(name='testerino2', id=1)
    assert mock_update.call_count == 1
    assert cmp(kwargs, env)
    assert result == 'buildenvironment1'

@patch('pnc_cli.environments._environment_exists', return_value=False)
@patch('pnc_cli.environments.envs_api.update')
def test_update_environment_notexist(mock_update, mock_environment_exists):
    result = environments.update_environment(id=1)
    mock_environment_exists.assert_called_once_with(1)
    assert not mock_update.called
    assert not result

@patch('pnc_cli.environments.get_environment_id', return_value=1)
@patch('pnc_cli.environments.envs_api.delete', return_value=True)
def test_delete_environment_id(mock_delete, mock_get_environment_id):
    result = environments.delete_environment(id=1)
    mock_get_environment_id.assert_called_once_with(1,None)
    mock_delete.assert_called_once_with(id=1)
    assert result

@patch('pnc_cli.environments.get_environment_id', return_value=1)
@patch('pnc_cli.environments.envs_api.delete', return_value=True)
def test_delete_environment_name(mock_delete, mock_get_environment_id):
    result = environments.delete_environment(name='testenv')
    mock_get_environment_id.assert_called_once_with(None,'testenv')
    mock_delete.assert_called_once_with(id=1)
    assert result

@patch('pnc_cli.environments.get_environment_id', return_value=None)
@patch('pnc_cli.environments.envs_api.delete')
def test_delete_environment_notexist(mock_delete, mock_get_environment_id):
    result = environments.delete_environment(id=1)
    mock_get_environment_id.assert_called_once_with(1,None)
    assert not mock_delete.called
    assert not result

@patch('pnc_cli.environments.get_environment_id', return_value=1)
@patch('pnc_cli.environments.envs_api.get_specific', return_value=MagicMock(content='buildenvironment1'))
def test_get_environment_id(mock_get_specific, mock_get_environment_id):
    result = environments.get_environment(id=1)
    mock_get_environment_id.assert_called_once_with(1,None)
    mock_get_specific.assert_called_once_with(id=1)
    assert result == 'buildenvironment1'

@patch('pnc_cli.environments.get_environment_id', return_value=1)
@patch('pnc_cli.environments.envs_api.get_specific', return_value=MagicMock(content='buildenvironment1'))
def test_get_environment_name(mock_get_specific, mock_get_environment_id):
    result = environments.get_environment(name='testerino')
    mock_get_environment_id.assert_called_once_with(None, 'testerino')
    mock_get_specific.assert_called_once_with(id=1)
    assert result == 'buildenvironment1'

@patch('pnc_cli.environments.get_environment_id', return_value=None)
@patch('pnc_cli.environments.envs_api.get_specific')
def test_get_environment_notexist(mock_get_specific, mock_get_environment_id):
    result = environments.get_environment(id=100)
    mock_get_environment_id.assert_called_once_with(100, None)
    assert not mock_get_specific.called
    assert not result

@patch('pnc_cli.environments.envs_api.get_all', return_value=MagicMock(content=['env1','env2','env3']))
def test_list_environments(mock):
    result = environments.list_environments()
    mock.assert_called_once_with()
    assert result == ['env1','env2','env3']

