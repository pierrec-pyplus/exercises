#!/usr/bin/env python
from pprint import pprint

'''
2. NAPALM Getters

2a. Create a new file named "my_functions.py" that will store a set of reusable
functions. Move the "open_napalm_connection" function from exercise1 into this
Python file. Import the network devices once again from my_devices.py and create
a list of connection objects (once again with connections to both cisco3 and
arista1).
'''
print("-" * 80)
print('Exercise 2a: ')
print("-" * 80)
print("Connect to devices")

from my_devices import cisco3, arista1
from my_functions import open_napalm_connection, create_backup

my_napalm_conn_list = []
my_napalm_conn_list.append(open_napalm_connection(cisco3))
my_napalm_conn_list.append(open_napalm_connection(arista1))

print("-" * 80)
input("Press Enter to continue...")
print()

'''
2b. Pretty print the arp table for each of these devices. Gather this
information using the appropriate NAPALM Getter.
'''
print("-" * 80)
print('Exercise 2b: ')
print("-" * 80)
print("Display ARP table")

# https://napalm.readthedocs.io/en/latest/support/index.html?__s=qpapvaan35h09675n74y#getters-support-matrix
# get_arp_table	
for my_napalm_conn in my_napalm_conn_list:
    print("=====")
    print(my_napalm_conn.get_facts()['hostname'])
    output = my_napalm_conn.get_arp_table()
    pprint(output)
    print("=====")
    print()

print("-" * 80)
input("Press Enter to continue...")
print()

'''
2c. Attempt to use the get_ntp_peers() method against both of the devices. Does
this method work? Your code should gracefully handle any exceptions that occur.
In other words, an exception that occurs due to this get_ntp_peers() method,
should not cause the program to crash.
'''
print("-" * 80)
print('Exercise 2c: ')
print("-" * 80)
print("Display NTP peers")

for my_napalm_conn in my_napalm_conn_list:
    print("=====")
    print(my_napalm_conn.get_facts()['hostname'])
    try:
        output = my_napalm_conn.get_ntp_peers()
    except NotImplementedError:
        output = "/!\ Not implemented for platform: " + my_napalm_conn.platform
    pprint(output)
    print("=====")
    print()

print("-" * 80)
input("Press Enter to continue...")
print()

'''
2d. Create another function in "my_functions.py". This function should be named
"create_backup" and should accept a NAPALM connection object as an argument.
Using the NAPALM get_config() method, the function should retrieve and write the
current running configuration to a file. The filename should be unique for each
device. In other words, "cisco3" and "arista1" should each have a separate file
that stores their running configuration. Note, get_config() returns a dictionary
where the running-config is referenced using the "running" key. Call this
function as part of your main exercise2 and ensure that the configurations
from both cisco3 and arista1 are backed up properly.
'''
print("-" * 80)
print('Exercise 2d: ')
print("-" * 80)
print("Create backup files")

for my_napalm_conn in my_napalm_conn_list:
    print("=====")
    print(my_napalm_conn.get_facts()['hostname'])
    create_backup(my_napalm_conn)
    print("=====")

print("-" * 80)
print()

# --------------------------------------------------------------------------------
# Exercise 2a: 
# --------------------------------------------------------------------------------
# Connect to devices
# Password: 
# opening connection to cisco3.lasthop.io
# opening connection to arista1.lasthop.io
# --------------------------------------------------------------------------------
# Press Enter to continue...
# 
# --------------------------------------------------------------------------------
# Exercise 2b: 
# --------------------------------------------------------------------------------
# Display ARP table
# =====
# cisco3
# [{'age': 1.0,
#   'interface': 'GigabitEthernet0/0/0',
#   'ip': '10.220.88.1',
#   'mac': '00:24:C4:E9:48:AE'},
#  {'age': 195.0,
#   'interface': 'GigabitEthernet0/0/0',
#   'ip': '10.220.88.21',
#   'mac': '1C:6A:7A:AF:57:6C'},
#  {'age': -1.0,
#   'interface': 'GigabitEthernet0/0/0',
#   'ip': '10.220.88.22',
#   'mac': 'A0:93:51:41:B7:80'},
#  {'age': 64.0,
#   'interface': 'GigabitEthernet0/0/0',
#   'ip': '10.220.88.28',
#   'mac': '00:AA:FC:05:B5:13'},
#  {'age': 199.0,
#   'interface': 'GigabitEthernet0/0/0',
#   'ip': '10.220.88.31',
#   'mac': '00:AC:FC:59:97:F2'},
#  {'age': 141.0,
#   'interface': 'GigabitEthernet0/0/0',
#   'ip': '10.220.88.37',
#   'mac': '00:01:00:FF:00:01'},
#  {'age': 175.0,
#   'interface': 'GigabitEthernet0/0/0',
#   'ip': '10.220.88.38',
#   'mac': '00:02:00:FF:00:01'}]
# =====
# 
# =====
# arista1
# [{'age': 0.0,
#   'interface': 'Vlan1, Ethernet1',
#   'ip': '10.220.88.1',
#   'mac': '00:24:C4:E9:48:AE'},
#  {'age': 0.0,
#   'interface': 'Vlan1, not learned',
#   'ip': '10.220.88.20',
#   'mac': 'C8:9C:1D:EA:0E:B6'},
#  {'age': 0.0,
#   'interface': 'Vlan1, not learned',
#   'ip': '10.220.88.22',
#   'mac': 'A0:93:51:41:B7:80'},
#  {'age': 0.0,
#   'interface': 'Vlan1, not learned',
#   'ip': '10.220.88.29',
#   'mac': '00:AF:FC:9A:E4:9E'},
#  {'age': 0.0,
#   'interface': 'Vlan1, not learned',
#   'ip': '10.220.88.30',
#   'mac': '00:AB:FC:C0:F9:7C'},
#  {'age': 0.0,
#   'interface': 'Vlan1, not learned',
#   'ip': '10.220.88.31',
#   'mac': '00:AC:FC:59:97:F2'},
#  {'age': 0.0,
#   'interface': 'Vlan1, not learned',
#   'ip': '10.220.88.37',
#   'mac': '00:01:00:FF:00:01'},
#  {'age': 0.0,
#   'interface': 'Vlan1, not learned',
#   'ip': '10.220.88.38',
#   'mac': '00:02:00:FF:00:01'}]
# =====
# 
# --------------------------------------------------------------------------------
# Press Enter to continue...
# 
# --------------------------------------------------------------------------------
# Exercise 2c: 
# --------------------------------------------------------------------------------
# Display NTP peers
# =====
# cisco3
# {'130.126.24.24': {}, '152.2.21.1': {}}
# =====
# 
# =====
# arista1
# '/!\\ Not implemented for platform: eos'
# =====
# 
# --------------------------------------------------------------------------------
# Press Enter to continue...
# 
# --------------------------------------------------------------------------------
# Exercise 2d: 
# --------------------------------------------------------------------------------
# Create backup files
# =====
# cisco3
# =====
# =====
# arista1
# =====
# --------------------------------------------------------------------------------
