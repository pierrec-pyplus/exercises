import pytest
from netmiko import ConnectHandler
from getpass import getpass

my_password = getpass()


@pytest.fixture(scope="module")
def net_connect(request):
    arista1 = {
        'host': 'arista1.lasthop.io',
        'username': 'pyclass',
        'password': my_password,
        'device_type': 'arista_eos',
        }
    my_conn = ConnectHandler(**arista1)
    
    def fin():
        my_conn.disconnect()

    request.addfinalizer(fin)    
    return my_conn
