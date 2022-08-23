#!/usr/bin/env python

'''
3. For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. Save this output to a file in the current working directory.
'''

from netmiko import ConnectHandler
from getpass import getpass

ios3 = {
    'host':'cisco3.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_ios',
    # 'session_log':'mysession.txt'
}

net_connect = ConnectHandler(**ios3)

show_version = net_connect.send_command('show version')

with open("show_version.txt", "w") as f:
    f.write(show_version)

