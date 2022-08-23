#!/usr/bin/env python

'''
7. Using your TextFSM template and the 'show interface status' data from exercise2, create a Python program that uses TextFSM to parse this data. In this Python program, read the show interface status data from a file and process it using the TextFSM template. From this parsed-output, create a list of dictionaries. The program output should look as follows:

 
$ python ex7_show_int_status.py 
 
[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/1',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/2',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/3',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'}]
'''

import textfsm
from pprint import pprint

# using TEXTFSM ro parse ex2_show_int_status.txt
template_file = "ex2_show_int_status.tpl"
template = open(template_file)
with open("ex2_show_int_status.txt") as f:
    raw_text_data = f.read()
# 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

# Formatting output DATA into a list of dicts
my_list = []
for line in data:
  #^${PORT_NAME}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${PORT_TYPE}\s*$$ -> Record
  # ['Gi0/1/0', 'notconnect', '1', 'auto', 'auto', '10/100/1000BaseTX']
  my_dict = {
    'DUPLEX': line[3],
    'PORT_NAME': line[0],
    'PORT_TYPE': line[5],
    'SPEED': line[4],
    'STATUS': line[1],
    'VLAN': line[2],
  }
  my_list.append(my_dict)

# Displaying OutPut DATA
print()
print("-" * 80)
pprint(my_list)
print("-" * 80)
print()
