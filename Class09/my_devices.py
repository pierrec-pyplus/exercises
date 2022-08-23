from getpass import getpass

# https://napalm.readthedocs.io/en/latest/support/index.html
my_passwd = getpass()

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "device_type": "ios",
    "username": "pyclass",
    "password": my_passwd,
    "optional_args": {},
        }

arista1 = {
    "hostname": "arista1.lasthop.io",
    "device_type": "eos",
    "username": "pyclass",
    "password": my_passwd,
    "optional_args": {},
        }

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "device_type": "nxos",
    "username": "pyclass",
    "password": my_passwd,
    "optional_args": {"port": 8443},
        }
