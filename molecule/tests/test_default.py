import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def get_mysql_version():
    return os.getenv('MYSQL_VERSION', '8.0.12')


def get_mysql_installer_filename(host):
    os = host.system_info.distribution
    if os.lower() in ['ubuntu', 'debian']:
        mysql_installer_filename = 'mysql-apt-config_0.8.10-1_all.deb'
    else:
        mysql_installer_filename = 'unknown'
    return mysql_installer_filename


def get_path_separator():
    return '/'


def get_temp_dir():
    return '/tmp'


@pytest.fixture(scope='module')
def test_vars(host):
    test_vars = {
        'mysql_version': get_mysql_version(),
        'mysql_installer_filename': get_mysql_installer_filename(host),
        'path_separator': get_path_separator(),
        'temp_dir': get_temp_dir()
    }
    return test_vars


def test_mysql_version_fact(host, test_vars):
    f = host.file(test_vars['temp_dir'] +
                  test_vars['path_separator'] + 'vars_log.txt')
    mysql_version_string = 'mysql_version=' + test_vars['mysql_version']
    assert f.exists
    assert f.contains(mysql_version_string)


def test_mysql_installer_filename_fact(host, test_vars):
    f = host.file(test_vars['temp_dir'] +
                  test_vars['path_separator'] + 'vars_log.txt')
    mysql_installer_filename_string = 'mysql_installer_filename=' + \
        test_vars['mysql_installer_filename']
    assert f.exists
    assert f.contains(mysql_installer_filename_string)
