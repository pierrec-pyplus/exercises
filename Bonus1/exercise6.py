#!/usr/bin/env python

'''
6. Use an HTTP DELETE and Python-requests to delete the IP address object that
you just created. Remember to reference the ID of your object.
'''

import os
import requests
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

# Select IP by ID (from exercise 4.a)
# {'address': '192.0.2.176/32',
#  'created': '2022-05-20',
#  'custom_fields': {},
#  'description': '',
#  'family': 4,
#  'id': 474,
#  'interface': None,
#  'last_updated': '2022-05-20T03:35:57.829612-07:00',
#  'nat_inside': None,
#  'nat_outside': None,
#  'role': None,
#  'status': {'label': 'Active', 'value': 1},
#  'tags': [],
#  'tenant': None,
#  'vrf': None}
url = "https://netbox.lasthop.io/api/ipam/ip-addresses/474/"

# Prepare the header for DELETE
http_headers = {
    "Content-Type": "application/json; version=2.4;",
    "authorization": "Token {}".format(token),
}

response = requests.delete(url, headers=http_headers, verify=False)

print()
# print(response)
# # <Response [204]>
if response.ok:
    print("Address deleted successfully")
else:
    print("Fail to delete address")
print()
 
# 
# Address deleted successfully
# 
