#!/usr/bin/env python

'''
In your lab environment, there is a file located at ~/.netmiko.yml. This file contains all of the devices used in the lab. Create a Python program that processes this YAML file and then uses Netmiko to connect to the Cisco3 router. Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs designed to work directly with Netmiko. The .netmiko.yml also contains group definitions for: cisco, arista, juniper, and nxos groups. These group definitions are lists of devices. Once again, don't check the .netmiko.yml into GitHub.
'''

import yaml
import os
from pprint import pprint
from netmiko import ConnectHandler

# filename parsing
filename = os.path.expanduser('~/.netmiko.yml')
my_dir = os.path.dirname(filename)
my_file = os.path.basename(filename)
os.chdir(my_dir)

# open yaml file
with open(my_file) as f:
    yaml_out = yaml.safe_load(f)

# select device to connect to
my_device = yaml_out['cisco3']

# connect & print banner
net_connect = ConnectHandler(**my_device)
print(net_connect.find_prompt())

