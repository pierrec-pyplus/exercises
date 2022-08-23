#!/usr/bin/env python

'''
1. Using the pyeapi library, connect to arista3.lasthop.io and execute 'show ip arp'. From this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
'''

import pyeapi
from pprint import pprint
from getpass import getpass

connection = pyeapi.client.connect(
        transport="https",
        host="arista3.lasthop.io",
        username = "pyclass",
        password = getpass(),
        port="443",
        )

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

