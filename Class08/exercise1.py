#!/usr/bin/env python

'''
1. PyEZ basic connection and facts:

1a. Create a PyEZ Device object from the jnpr.junos Device class. This device
object should connect to "srx2.lasthop.io". Use getpass() to enter the device's
password. Pretty print all of the device's facts. Additionally, retrieve and
print only the "hostname" fact.
'''

from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

print("-" * 80)
print('Exercise 1a: ')
print("-" * 80)
a_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
a_device.open()
my_facts = a_device.facts
pprint(my_facts)
print()
print(f"hostname is: {my_facts['hostname']}")
print("-" * 80)
print()

# --------------------------------------------------------------------------------
# Exercise 1a: 
# --------------------------------------------------------------------------------
# Password: 
# {'2RE': False,
#  'HOME': '/var/home/pyclass',
#  'RE0': {'last_reboot_reason': '0x1:power cycle/failure',
#          'mastership_state': 'master',
#          'model': 'RE-SRX110H2-VA',
#          'status': 'OK',
#          'up_time': '325 days, 11 hours, 40 minutes, 30 seconds'},
#  'RE1': None,
#  'RE_hw_mi': False,
#  'current_re': ['master',
#                 'node',
#                 'fwdd',
#                 'member',
#                 'pfem',
#                 'backup',
#                 're0',
#                 'fpc0.pic0'],
#  'domain': None,
#  'fqdn': 'srx2',
#  'hostname': 'srx2',
#  'hostname_info': {'re0': 'srx2'},
#  'ifd_style': 'CLASSIC',
#  'junos_info': {'re0': {'object': junos.version_info(major=(12, 1), type=X, minor=(46, 'D', 35), build=1),
#                         'text': '12.1X46-D35.1'}},
#  'master': 'RE0',
#  'model': 'SRX110H2-VA',
#  'model_info': {'re0': 'SRX110H2-VA'},
#  'personality': 'SRX_BRANCH',
#  're_info': {'default': {'0': {'last_reboot_reason': '0x1:power cycle/failure',
#                                'mastership_state': 'master',
#                                'model': 'RE-SRX110H2-VA',
#                                'status': 'OK'},
#                          'default': {'last_reboot_reason': '0x1:power '
#                                                            'cycle/failure',
#                                      'mastership_state': 'master',
#                                      'model': 'RE-SRX110H2-VA',
#                                      'status': 'OK'}}},
#  're_master': {'default': '0'},
#  'serialnumber': 'CA2418AF0190',
#  'srx_cluster': False,
#  'srx_cluster_id': None,
#  'srx_cluster_redundancy_group': None,
#  'switch_style': 'VLAN',
#  'vc_capable': False,
#  'vc_fabric': None,
#  'vc_master': None,
#  'vc_mode': None,
#  'version': '12.1X46-D35.1',
#  'version_RE0': '12.1X46-D35.1',
#  'version_RE1': None,
#  'version_info': junos.version_info(major=(12, 1), type=X, minor=(46, 'D', 35), build=1),
#  'virtual': False}
# 
# hostname is: srx2
# --------------------------------------------------------------------------------
# 
