#!/usr/bin/env python

'''
4. Use lxml to find() elements in an XML tree
'''
from lxml import etree

'''
4a. Use the find() method to retrieve the first "zones-security" element. Print out the tag of this element and of all its children elements. Your output should be similar to the following:

 
Find tag of the first zones-security element
--------------------
zones-security
 
Find tag of all child elements of the first zones-security element
--------------------
zones-security-zonename
zones-security-send-reset
zones-security-policy-configurable
zones-security-interfaces-bound
zones-security-interfaces
'''
print("-" * 80)
print('Exercise 4a: ')
print("-" * 80)

my_xml = etree.parse("show_security_zones.xml")
# my_xml = my_xml.getroot()

print('Find tag of the first zones-security element')
print("-" * 20)
print(my_xml.find("zones-security").tag)
print()
print('Find tag of all child elements of the first zones-security element')
print("-" * 20)
for node in my_xml.find("zones-security").iterchildren():
    print(node.tag)
print("-" * 80)
input("Press a key to continue...")
print()

'''
4b. Use the find() method to find the first "zones-security-zonename". Print out the zone name for that element (the "text" of that element).
'''
print("-" * 80)
print('Exercise 4b: ')
print("-" * 80)

# using xpath method ".//" to browse the tree
print(my_xml.find(".//zones-security-zonename").text)

print("-" * 80)
input("Press a key to continue...")
print()

'''
4c. Use the findall() method to find all occurrences of "zones-security". For each of these security zones, print out the security zone name ("zones-security-zonename", the text of that element).
'''
print("-" * 80)
print('Exercise 4c: ')
print("-" * 80)

# print(etree.tostring(my_xml).decode()) 
for elmnts in my_xml.findall(".//zones-security"):
    print(elmnts.find("zones-security-zonename").text) 

print("-" * 80)
print()

