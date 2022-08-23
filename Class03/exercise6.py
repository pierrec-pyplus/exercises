#!/usr/bin/env python

'''
Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. Print out the interface name and IP address for each interface. Your solution should work if there is more than one IP address configured on Cisco4. For example, if you configure a loopback interface on Cisco4 with an IP address, then your solution should continue to work. The output from this program should look similar to the following:

 
$ python confparse_ex6.py 
 
Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0
'''

from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse

cisco4 = {
    'host':'cisco4.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_ios',
    # 'session_log':'mysession.txt'
}

net_connect = ConnectHandler(**cisco4)

command = "show runn"

output = net_connect.send_command(command)

cisco_obj = CiscoConfParse(output.splitlines())

match = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\sip address")

for child in match:
  if_name = child.text
  ip_address = child.re_search_children(r"ip address")[0].text
  print()
  print("Interface Line: " + if_name)
  print("IP Address Line: " + ip_address)
  print()

