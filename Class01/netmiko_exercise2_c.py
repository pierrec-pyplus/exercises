#!/usr/bin/env python

'''
2. Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices. Additionally, use a for-loop to accomplish the Netmiko connection creation. Once again print the prompt back from the devices that you connected to.
'''

from netmiko import ConnectHandler
from getpass import getpass

my_password = getpass()

nxos1 = {
        'host': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': my_password,
        'device_type': 'cisco_nxos'
        }

nxos2 = {
        'host': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': my_password,
        'device_type': 'cisco_nxos'
        }

my_devices = [ nxos1, nxos2 ]

for devices in my_devices:
    net_connect = ConnectHandler(**devices)
    print("-" * 30)
    print(net_connect.find_prompt())
    print("-" * 30)

