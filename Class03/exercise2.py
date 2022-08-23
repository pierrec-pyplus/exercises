#!/usr/bin/env python

'''
2a. Create a list where each of the list elements is a dictionary representing one of the network devices in the lab. Do this for at least four of the lab devices. The dictionary should have keys corresponding to the device_name, host (i.e. FQDN), username, and password. Use a fictional username/password to avoid checking the lab password into GitHub.

2b. Write the data structure you created in part 2a out to a YAML file. Use expanded YAML format. How could you re-use this YAML file later when creating Netmiko connections to devices?
'''

from pprint import pprint
import yaml

my_list = [
    { 'device_name': 'cisco3',
    'host': 'cisco3.lasthop.io',
    'username': 'lab_user1', 
    'password': 'lab_passwd1', },
    
    { 'device_name': 'cisco4',
    'host': 'cisco4.lasthop.io',
    'username': 'lab_user1', 
    'password': 'lab_passwd1', },
    
    { 'device_name': 'arista1',
    'host': 'arista1.lasthop.io',
    'username': 'lab_user1', 
    'password': 'lab_passwd1', },

    { 'device_name': 'arista2',
    'host': 'arista2.lasthop.io',
    'username': 'lab_user1', 
    'password': 'lab_passwd1', },
]

# pprint(my_list)

filename = "exercise2.yml"
with open(filename, "wt") as f:
    # expanded format: prefered !!
    yaml.dump(my_list, f, default_flow_style=False)

#
# reuse of this file later on
#

with open(filename) as f:
    yaml_out = yaml.safe_load(f)

# pprint(yaml_out)

for my_device in yaml_out:
    pprint(my_device)
# need to add device type and may be remove 'host' key
#   net_connect = ConnectHandler(**my_device)

