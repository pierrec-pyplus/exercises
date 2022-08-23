#!/usr/bin/env python

'''
5. Building on the script from exercise 4, add a description to the the IP
address object that you just created. Accomplish this using an HTTP PUT. The
HTTP PUT operation will require all of the mandatory fields in the object (in
this case, the "address" field). Print the status code and the response.json()
from your PUT operation. The HTTP PUT operation will use same URL as exercise
4b (i.e. the URL of the newly created IP address object including its ID).
'''

import os
import requests
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

# First read the data
http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"
http_headers["authorization"] = f"Token {token}"
url = "https://netbox.lasthop.io/api/ipam/ip-addresses/474/"

response = requests.get(url, headers=http_headers, verify=False)
my_ipaddr = response.json()
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

# Prepare the header for PUT
http_headers = {
    "Content-Type": "application/json; version=2.4;",
    "authorization": "Token {}".format(token),
}

my_descr = {
    'address': my_ipaddr['address'],
    'description': 'added by Pete',
}

response = requests.put(
    url, headers=http_headers, data=json.dumps(my_descr), verify=False
)
response = response.json()
print()
pprint(response)
print()

# {'address': '192.0.2.176/32',
#  'created': '2022-05-20',
#  'custom_fields': {},
#  'description': 'added by Pete',
#  'family': 4,
#  'id': 474,
#  'interface': None,
#  'last_updated': '2022-05-25T05:12:10.076585-07:00',
#  'nat_inside': None,
#  'nat_outside': None,
#  'role': None,
#  'status': {'label': 'Active', 'value': 1},
#  'tags': [],
#  'tenant': None,
#  'vrf': None}
# 
