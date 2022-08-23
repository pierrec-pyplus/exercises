#!/usr/bin/env python

'''
4a. Using an HTTP POST and the Python-requests library, create a new IP address
in NetBox. This IP address object should be a /32 from the 192.0.2.0/24
documentation block. Print out the status code and the returned JSON.
'''
import requests
from pprint import pprint
import os
import json

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]
### 4.a ###
http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"
url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"
data = {"address": "192.0.2.176/32"}

response = requests.post(url, headers=http_headers, data=json.dumps(data), verify=False)
response = response.json()
print()
pprint(response)
print()

# {'address': '192.0.2.176/32',
#  'created': '2022-05-20',
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
