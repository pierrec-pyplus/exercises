#!/usr/bin/env python

'''
2. xmltodict basics
'''

import xmltodict
from pprint import pprint
'''
2a. Using xmltodict, load the show_security_zones.xml file as a Python
dictionary. Print out this new variable and its type. Note, the newly created
object is an OrderedDict; not a traditional dictionary.
'''
print("-" * 80)
print('Exercise 2a: ')
print("-" * 80)

xml_file = open("show_security_zones.xml")
xml_data = xml_file.read().strip()
xml_file.close()

xml_dict = xmltodict.parse(xml_data)
pprint(xml_dict)
print()

print(f"variable type is : {type(xml_dict)}")
print()
print("-" * 80)
input("Press a key to continue...")
print()

'''
2b. Print the names and an index number of each security zone in the XML data
from Exercise 2a. Your output should look similar to the following (tip,
enumerate will probably help):
 
Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host
'''
print("-" * 80)
print('Exercise 2a: ')
print("-" * 80)
i = 1
for zone in xml_dict["zones-information"]["zones-security"]:
    print(f"Security Zone #{i}: {zone['zones-security-zonename']}")
    i += 1
print("-" * 80)
print()
