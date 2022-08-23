#!/usr/bin/env python

'''
2a. Define an Arista device in an external YAML file (use arista4.lasthop.io for the device). In your YAML file, make sure the key names exactly match the names required for use with pyeapi and the connect() method. In other words, you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from your YAML file. Do not store the lab password in this YAML file, instead set the password using getpass() in your Python program. Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi. Once again, from this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
'''

from pprint import pprint
from getpass import getpass
import yaml
import pyeapi


filename = "my_device.yml"

with open(filename) as f:
    yaml_out = yaml.safe_load(f)

passwd = getpass("Password: ")

for device_dict in yaml_out:
    device_dict.update({"password": passwd})
    
    connection = pyeapi.client.connect(**device_dict)

    device = pyeapi.client.Node(connection)
    output = device.enable("show ip arp")

    print()
    print("-" * 80)
    for my_dict in output[0]['result']['ipV4Neighbors']:
        my_addr = my_dict["address"]
        my_mac = my_dict["hwAddress"]
        print(f'IP addr: {my_addr} - MAC: {my_mac}')

    print("-" * 80)
    print()

