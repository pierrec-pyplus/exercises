#!/usr/bin/env python

'''
Use Netmiko and the send_config_set() method to configure the following
on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with fast_cli=True to see how long the script takes to execute
(with and without this option enabled).

Verify DNS lookups on the router are now working by executing 'ping
google.com'. Verify from this that you receive a ping response back.
'''

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = {
    'host':'cisco3.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_ios',
#   'fast_cli' default seems to be True
    'fast_cli':False,
}

my_cmd = 'ping www.google.it'

my_cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup',
]

net_connect = ConnectHandler(**device1)
print()
print("-" * 80)
print(net_connect.find_prompt())
print("-" * 80)

# INITIAL TEST
output = net_connect.send_command(my_cmd)
print()
print("-" * 80)
print(output)
print("-" * 80)

# CONFIG
start_time = datetime.now()
output = net_connect.send_config_set(my_cfg)
end_time = datetime.now()
print()
print("-" * 80)
print(output)
print()
delay = end_time - start_time
print("delay in sec = ",  delay.total_seconds())
print("-" * 80)

# TEST
output = net_connect.send_command(my_cmd)
print()
print("-" * 80)
print(output)
print("-" * 80)

net_connect.disconnect()

