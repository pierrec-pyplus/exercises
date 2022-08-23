#!/usr/bin/env python

'''
You have the following JSON ARP data from an Arista switch:

 
{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "dc38.e111.97cf",
            "address": "172.17.17.1",
            "interface": "Ethernet45",
            "age": 0
        },
        {
            "hwAddress": "90e2.ba5c.25fd",
            "address": "172.17.16.1",
            "interface": "Ethernet36",
            "age": 0
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
}

From a file, read this JSON data into your Python program. Process this ARP data and return a dictionary where the dictionary keys are the IP addresses and the dictionary values are the MAC addresses. Print this dictionary to standard output.
'''

import json
from pprint import pprint

with open("exercise4.json") as f:
    data = json.load(f)

my_arp = {}

for arp_entry in data['ipV4Neighbors']:
    ip_addr = arp_entry['address']
    mac_addr = arp_entry['hwAddress']
    my_arp.update({ip_addr: mac_addr})

print()
pprint(my_arp)
print()

