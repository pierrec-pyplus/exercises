#!/usr/bin/env python
from napalm import get_network_driver
from pprint import pprint
'''
1. Simple NAPALM Connections and Facts

1a. Create a Python file named "my_devices.py" that defines the NAPALM
connection information for both the 'cisco3' device and the 'arista1' device.
Use getpass() for the password handling. This Python module should be used to
store the device connection information for all of the exercises in this lesson.
'''
print("-" * 80)
print('Exercise 1a: ')
print("-" * 80)

from my_devices import cisco3, arista1

print("-" * 80)
input("Press Enter to continue...")
print()

'''
1b. Create a simple function that accepts the NAPALM device information from the
my_devices.py file and creates a NAPALM connection object. This function should
open the NAPALM connection to the device and should return the NAPALM connection
object.
'''
print("-" * 80)
print('Exercise 1b: ')
print("-" * 80)

def open_napalm_connection(my_device):
    device_type = my_device.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**my_device)
    print(f"opening connection to {my_device['hostname']}")
    device.open()
    return device

print("-" * 80)
input("Press Enter to continue...")
print()

'''
1c. Using your "my_devices.py" file and your NAPALM connection function, create
a list of NAPALM connection objects to 'cisco3' and 'arista1'.
'''
print("-" * 80)
print('Exercise 1c: ')
print("-" * 80)

my_napalm_conn_list = []

my_napalm_conn_list.append(open_napalm_connection(cisco3))
my_napalm_conn_list.append(open_napalm_connection(arista1))

print("-" * 80)
input("Press Enter to continue...")
print()

'''
1d. Iterate through the connection objects, print out the device's connection
object itself. Additionally, pretty print the facts for each device and also
print out the device's NAPALM platform type (ios, eos, et cetera).
'''
print("-" * 80)
print('Exercise 1d: ')
print("-" * 80)

for my_conn_obj in my_napalm_conn_list:
    print()
    print(f"Connection object: {my_conn_obj}")
    print(f"Platform type: {my_conn_obj.platform}")
    print("Facts:")
    pprint(my_conn_obj.get_facts())
    print("-" * 20)
print("-" * 80)
print()
# --------------------------------------------------------------------------------
# Exercise 1a: 
# --------------------------------------------------------------------------------
# Password: 
# --------------------------------------------------------------------------------
# Press Enter to continue...
# 
# --------------------------------------------------------------------------------
# Exercise 1b: 
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# Press Enter to continue...
# 
# --------------------------------------------------------------------------------
# Exercise 1c: 
# --------------------------------------------------------------------------------
# opening connection to cisco3.lasthop.io
# opening connection to arista1.lasthop.io
# --------------------------------------------------------------------------------
# Press Enter to continue...
# 
# --------------------------------------------------------------------------------
# Exercise 1d: 
# --------------------------------------------------------------------------------
# 
# Connection object: <napalm.ios.ios.IOSDriver object at 0x7f24f5c52450>
# Platform type: ios
# Facts:
# {'fqdn': 'cisco3.not set',
#  'hostname': 'cisco3',
#  'interface_list': ['GigabitEthernet0/0/0',
#                     'GigabitEthernet0/0/1',
#                     'GigabitEthernet0/1/0',
#                     'GigabitEthernet0/1/1',
#                     'GigabitEthernet0/1/2',
#                     'GigabitEthernet0/1/3',
#                     'Vlan1'],
#  'model': 'C1111-4P',
#  'os_version': 'ISR Software (ARMV8EL_LINUX_IOSD-UNIVERSALK9_IAS-M), Version '
#                '16.12.3, RELEASE SOFTWARE (fc5)',
#  'serial_number': 'FGL222290LB',
#  'uptime': 658680,
#  'vendor': 'Cisco'}
# --------------------
# 
# Connection object: <napalm.eos.eos.EOSDriver object at 0x7f24f49fdf50>
# Platform type: eos
# Facts:
# {'fqdn': 'arista1',
#  'hostname': 'arista1',
#  'interface_list': ['Ethernet1',
#                     'Ethernet2',
#                     'Ethernet3',
#                     'Ethernet4',
#                     'Ethernet5',
#                     'Ethernet6',
#                     'Ethernet7',
#                     'Management1',
#                     'Vlan1'],
#  'model': 'vEOS',
#  'os_version': '4.20.10M-10040268.42010M',
#  'serial_number': '',
#  'uptime': 1889307,
#  'vendor': 'Arista'}
# --------------------
# --------------------------------------------------------------------------------
