#!/usr/bin/env python

'''
On both the NXOS1 and NXOS2 switches configure five VLANs including
VLAN names (just pick 5 VLAN numbers between 100 - 999). Use Netmiko's
send_config_from_file() method to accomplish this. Also use Netmiko's
save_config() method to save the changes to the startup-config.
'''

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':password,
    'device_type':'cisco_nxos',
}

device2 = {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':password,
    'device_type':'cisco_nxos',
}

devices = [ device1, device2 ]

for my_device in devices:
    net_connect = ConnectHandler(**my_device)
    output = net_connect.send_config_from_file(config_file='netmiko_exercise5.txt')
    print()
    print("-" * 80)
    print(net_connect.find_prompt())
    print(output)
    save_out = net_connect.save_config()
    print()
    print(save_out)
    print("-" * 80)
    net_connect.disconnect()
