#!/usr/bin/env python

'''
1. Reading and accessing an XML file:
'''

from lxml import etree

'''
1a. Using the show_security_zones.xml file, read the file contents and parse the
file using etree.fromstring(). Print out the newly created XML variable and also
print out the variable's type. Your output should look similar to the following:
<Element zones-information at 0x7f3271194b48>
<class 'lxml.etree._Element'>
'''
print("-" * 80)
print('Exercise 1a: ')
print("-" * 80)
f = open("show_security_zones.xml")
xml_string = f.read().strip()
f.close()
my_xml = etree.fromstring(xml_string)    
print(my_xml)    
print(type(my_xml))    
print("-" * 80)
input("Press a key to continue...")
print()
'''
1b. Using your XML variable from exercise 1a, print out the entire XML tree in
a readable format (ensure that the output string is a unicode string).
'''
print("-" * 80)
print('Exercise 1b: ')
print("-" * 80)
xml_tree = etree.tostring(my_xml).decode()
print(xml_tree)
print("-" * 80)
input("Press a key to continue...")
print()
'''
1c. Print out the root element tag name (this tag should have a value of
"zones-information"). Print the number of child elements of the root element
(you can retrieve this using the len() function).
'''
print("-" * 80)
print('Exercise 1c: ')
print("-" * 80)
print(f"root element tag name is: {my_xml.tag}")
child_list = my_xml.getchildren()
print(f"number of child elements of the root element: {len(child_list)}")
print("-" * 80)
input("Press a key to continue...")
print()
'''
1d. Using both direct indices and the getchildren() method, obtain the first
child element and print its tag name.
'''
print("-" * 80)
print('Exercise 1d: ')
print("-" * 80)
# getchildren() method
first_child_element = my_xml.getchildren()[0]
print(f"first child tag name is: {first_child_element.tag}")
# direct indices method
first_child_element = my_xml[0]
print(f"first child tag name is: {first_child_element.tag}")
print("-" * 80)
input("Press a key to continue...")
print()
'''
1e. Create a variable named "trust_zone". Assign this variable to be the first
"zones-security" element in the XML tree. Access this newly created variable and
print out the text of the "zones-security-zonename" child.
'''
print("-" * 80)
print('Exercise 1e: ')
print("-" * 80)
trust_zone = my_xml.find("zones-security")
print(trust_zone.find("zones-security-zonename").text)
print("-" * 80)
input("Press a key to continue...")
print()
'''
1f. Iterate through all of the child elements of the "trust_zone" variable.
Print out the tag name for each child element.
'''
print("-" * 80)
print('Exercise 1f: ')
print("-" * 80)
for child in trust_zone.iterchildren(): 
    print(child.tag) 
print("-" * 80)
print()
