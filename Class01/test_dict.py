#!/usr/bin/env python3

'''
DESCRIPTION stands here

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

print(net_connect.find_prompt())

