import pytest
from netmiko import ConnectHandler
from getpass import getpass

my_password = getpass()


@pytest.fixture(scope="module")
def net_connect():
    arista1 = {
        'host': 'arista1.lasthop.io',
        'username': 'pyclass',
        'password': my_password,
        'device_type': 'arista_eos',
        }
    my_conn = ConnectHandler(**arista1)
    return my_conn

def test_prompt(net_connect):
    output = net_connect.find_prompt()
    assert "arista1" in output

def test_show_version(net_connect):
    output = net_connect.send_command('show version')
    assert "4.20.10M" in output

# (py3_venv) [cucurullo@pylab28a test_ex3]$ py.test -s -v test_netmiko_fixture.py
# ==================================================================== test session starts =====================================================================
# platform linux -- Python 3.7.10, pytest-7.0.1, pluggy-1.0.0 -- /home/cucurullo/VENV/py3_venv/bin/python3
# cachedir: .pytest_cache
# rootdir: /home/cucurullo/Bonus2/test_ex3
# plugins: pylama-8.3.7
# collecting ... Password: 
# collected 2 items                                                                                                                                            
# 
# test_netmiko_fixture.py::test_prompt PASSED
# test_netmiko_fixture.py::test_show_version PASSED
# 
# ===================================================================== 2 passed in 7.34s ======================================================================
# 
