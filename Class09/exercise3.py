#!/usr/bin/env python
from pprint import pprint

'''
3. NAPALM Config Merge

3a. Using your existing functions and the my_devices.py file, create a NAPALM
connection to both cisco3 and arista1.
'''
print("-" * 80)
print('Exercise 3a: ')
print("-" * 80)
print("Connect to devices using NAPALM")

from my_devices import cisco3, arista1
from my_functions import open_napalm_connection

my_napalm_conn_list = []
my_napalm_conn_list.append(open_napalm_connection(cisco3))
my_napalm_conn_list.append(open_napalm_connection(arista1))


print("-" * 80)
input("Press Enter to continue...")
print()

'''
3b. Create two new text files `arista1.lasthop.io-loopbacks` and 
`cisco3.lasthop.io-loopbacks`. In each of these files, create two new loopback
interfaces with a description. Your files should be similar to the following:

interface loopback100
  description loopback100
!
interface loopback101
  description loopback101

For both cisco3 and arista1, use the load_merge_candidate() method to stage the
candidate configuration. In other words, use load_merge_candidate() and your
loopback configuration file to stage a configuration change. Use the NAPALM
compare_config() method to print out the pending differences (i.e. the
differences between the running configuration and the candidate configuration).
'''
print("-" * 80)
print('Exercise 3b: ')
print("-" * 80)
print("Staging configs")

for my_napalm_conn in my_napalm_conn_list:
    print("=====")
    my_hostname = my_napalm_conn.get_facts()['hostname']
    print(my_hostname)
    my_filename = my_hostname + ".lasthop.io-loopbacks"
    my_napalm_conn.load_merge_candidate(filename=my_filename)
    print("---Display diff---")
    print(my_napalm_conn.compare_config())
    print("---Display diff---")
    print("=====")
    print()

print("-" * 80)
input("Press Enter to continue...")
print()

'''
3c. Commit the pending changes to each device, and check the diff once again
(after the commit_config).
'''
print("-" * 80)
print('Exercise 3c: ')
print("-" * 80)
print("Commit configs")

for my_napalm_conn in my_napalm_conn_list:
    print("=====")
    my_hostname = my_napalm_conn.get_facts()['hostname']
    print(my_hostname)
    print(my_napalm_conn.commit_config())
    print("---Display diff---")
    print(my_napalm_conn.compare_config())
    print("---Display diff---")
    print("=====")
    print()

print("-" * 80)
print()

# --------------------------------------------------------------------------------
# Exercise 3a: 
# --------------------------------------------------------------------------------
# Connect to devices using NAPALM
# Password: 
# opening connection to cisco3.lasthop.io
# opening connection to arista1.lasthop.io
# --------------------------------------------------------------------------------
# Press Enter to continue...
# 
# --------------------------------------------------------------------------------
# Exercise 3b: 
# --------------------------------------------------------------------------------
# Staging configs
# =====
# cisco3
# ---Display diff---
# +interface Loopback76
# + description loopback76
# +interface Loopback176
# + description loopback176
# ---Display diff---
# =====
# 
# =====
# arista1
# ---Display diff---
# @@ -45,6 +45,12 @@
#  interface Ethernet7
#     switchport access vlan 7
#  !
# +interface Loopback76
# +   description loopback76
# +!
# +interface Loopback176
# +   description loopback176
# +!
#  interface Management1
#     shutdown
#  !
# ---Display diff---
# =====
# 
# --------------------------------------------------------------------------------
# Press Enter to continue...
# 
# --------------------------------------------------------------------------------
# Exercise 3c: 
# --------------------------------------------------------------------------------
# Commit configs
# =====
# cisco3
# None
# ---Display diff---
# 
# ---Display diff---
# =====
# 
# =====
# arista1
# None
# ---Display diff---
# 
# ---Display diff---
# =====
# 
# --------------------------------------------------------------------------------
