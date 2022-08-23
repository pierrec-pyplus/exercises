#!/usr/bin/env python

'''
2a. Using the Python requests library, perform an HTTP GET on the base URL of
the NetBox server (https://netbox.lasthop.io/api/). Ensure that you are not
verifying the SSL certificate. Print the HTTP status code, the response text,
the JSON response, and the HTTP response headers. These items can be accessed
using the following attributes/methods in the Python-requests Response object:

response.status_code
response.text
response.json()
response.headers
'''

import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url = "https://netbox.lasthop.io/api/"
### 2.b ###
http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"
### 2.b ###
response = requests.get(url, headers=http_headers, verify=False)
print()
print("-" * 80)
print(f"Status code is: {response.status_code}")
print("-" * 80)
print()
print("-" * 80)
print(f"Text is: {response.text}")
print("-" * 80)
print()
print("-" * 80)
print(f"JSON is: {response.json()}")
print("-" * 80)
print()
print("-" * 80)
print(f"Headers are: {response.headers}")
print("-" * 80)
print()

### 2.c ###
url = "https://netbox.lasthop.io/api/dcim"
response = requests.get(url, headers=http_headers, verify=False)
pprint(response.json())
### 2.c ###

# --------------------------------------------------------------------------------
# Status code is: 200
# --------------------------------------------------------------------------------
# 
# --------------------------------------------------------------------------------
# Text is: {"circuits":"http://netbox.lasthop.io/api/circuits/","dcim":"http://netbox.lasthop.io/api/dcim/","extras":"http://netbox.lasthop.io/api/extras/","ipam":"http://netbox.lasthop.io/api/ipam/","secrets":"http://netbox.lasthop.io/api/secrets/","tenancy":"http://netbox.lasthop.io/api/tenancy/","virtualization":"http://netbox.lasthop.io/api/virtualization/"}
# --------------------------------------------------------------------------------
# 
# --------------------------------------------------------------------------------
# JSON is: {'circuits': 'http://netbox.lasthop.io/api/circuits/', 'dcim': 'http://netbox.lasthop.io/api/dcim/', 'extras': 'http://netbox.lasthop.io/api/extras/', 'ipam': 'http://netbox.lasthop.io/api/ipam/', 'secrets': 'http://netbox.lasthop.io/api/secrets/', 'tenancy': 'http://netbox.lasthop.io/api/tenancy/', 'virtualization': 'http://netbox.lasthop.io/api/virtualization/'}
# --------------------------------------------------------------------------------
# 
# --------------------------------------------------------------------------------
# Headers are: {'Server': 'nginx', 'Date': 'Fri, 20 May 2022 09:25:25 GMT', 'Content-Type': 'application/json', 'Content-Length': '353', 'Connection': 'keep-alive', 'Vary': 'Accept, Cookie, Origin', 'Allow': 'GET, HEAD, OPTIONS', 'API-Version': '2.4', 'X-Frame-Options': 'SAMEORIGIN', 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload'}
# --------------------------------------------------------------------------------
# 
# {'_choices': 'http://netbox.lasthop.io/api/dcim/_choices/',
#  'connected-device': 'http://netbox.lasthop.io/api/dcim/connected-device/',
#  'console-connections': 'http://netbox.lasthop.io/api/dcim/console-connections/',
#  'console-port-templates': 'http://netbox.lasthop.io/api/dcim/console-port-templates/',
#  'console-ports': 'http://netbox.lasthop.io/api/dcim/console-ports/',
#  'console-server-port-templates': 'http://netbox.lasthop.io/api/dcim/console-server-port-templates/',
#  'console-server-ports': 'http://netbox.lasthop.io/api/dcim/console-server-ports/',
#  'device-bay-templates': 'http://netbox.lasthop.io/api/dcim/device-bay-templates/',
#  'device-bays': 'http://netbox.lasthop.io/api/dcim/device-bays/',
#  'device-roles': 'http://netbox.lasthop.io/api/dcim/device-roles/',
#  'device-types': 'http://netbox.lasthop.io/api/dcim/device-types/',
#  'devices': 'http://netbox.lasthop.io/api/dcim/devices/',
#  'interface-connections': 'http://netbox.lasthop.io/api/dcim/interface-connections/',
#  'interface-templates': 'http://netbox.lasthop.io/api/dcim/interface-templates/',
#  'interfaces': 'http://netbox.lasthop.io/api/dcim/interfaces/',
#  'inventory-items': 'http://netbox.lasthop.io/api/dcim/inventory-items/',
#  'manufacturers': 'http://netbox.lasthop.io/api/dcim/manufacturers/',
#  'platforms': 'http://netbox.lasthop.io/api/dcim/platforms/',
#  'power-connections': 'http://netbox.lasthop.io/api/dcim/power-connections/',
#  'power-outlet-templates': 'http://netbox.lasthop.io/api/dcim/power-outlet-templates/',
#  'power-outlets': 'http://netbox.lasthop.io/api/dcim/power-outlets/',
#  'power-port-templates': 'http://netbox.lasthop.io/api/dcim/power-port-templates/',
#  'power-ports': 'http://netbox.lasthop.io/api/dcim/power-ports/',
#  'rack-groups': 'http://netbox.lasthop.io/api/dcim/rack-groups/',
#  'rack-reservations': 'http://netbox.lasthop.io/api/dcim/rack-reservations/',
#  'rack-roles': 'http://netbox.lasthop.io/api/dcim/rack-roles/',
#  'racks': 'http://netbox.lasthop.io/api/dcim/racks/',
#  'regions': 'http://netbox.lasthop.io/api/dcim/regions/',
#  'sites': 'http://netbox.lasthop.io/api/dcim/sites/',
#  'virtual-chassis': 'http://netbox.lasthop.io/api/dcim/virtual-chassis/'}
