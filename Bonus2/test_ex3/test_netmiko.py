from netmiko import ConnectHandler
from getpass import getpass

my_password = getpass()

arista1 = {
        'host': 'arista1.lasthop.io',
        'username': 'pyclass',
        'password': my_password,
        'device_type': 'arista_eos'
        }

def net_connect(my_device):
   my_conn = ConnectHandler(**my_device)
   return my_conn

def test_conn():
    conn = net_connect(arista1)
    output = conn.find_prompt()
    assert "arista1" in output

def test_show_version():
    conn = net_connect(arista1)
    output = conn.send_command('show version')
    assert "4.20.10M" in output

# (py3_venv) [cucurullo@pylab28a test_ex3]$ py.test -s -v test_netmiko.py 
# ==================================================================== test session starts =====================================================================
# platform linux -- Python 3.7.10, pytest-7.0.1, pluggy-1.0.0 -- /home/cucurullo/VENV/py3_venv/bin/python3
# cachedir: .pytest_cache
# rootdir: /home/cucurullo/Bonus2/test_ex3
# plugins: pylama-8.3.7
# collecting ... Password: 
# collected 2 items                                                                                                                                            
# 
# test_netmiko.py::test_conn PASSED
# test_netmiko.py::test_show_version PASSED
# 
# ===================================================================== 2 passed in 9.79s ======================================================================
# 
