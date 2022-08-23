#!/usr/bin/env python

'''
4b. Using the response data from the HTTP POST that created the IP address entry
in exercise 4a, capture the "id" of the newly created IP address object. Using
this ID, construct a new URL. Use this new URL and the HTTP GET method to
retrieve only the API information specific to this IP address.
'''
import requests
from pprint import pprint
import os

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"
url = "https://netbox.lasthop.io/api/ipam/ip-addresses/474/"

response = requests.get(url, headers=http_headers, verify=False)
response = response.json()
print()
pprint(response)
print()

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
