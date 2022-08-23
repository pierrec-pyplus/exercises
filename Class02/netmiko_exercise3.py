#!/usr/bin/env python

'''
On your AWS lab server, look at the ntc-templates index file (at
~/ntc-templates/templates/index). Look at some of the commands available for
cisco_ios (you can use 'cat ~/ntc-templates/templates/index | grep cisco_ios'
to see this). Also look at some of the abbreviated forms of Cisco IOS commands
that are supported in the index file.

Create a script using Netmiko that executes 'show version' and 'show lldp
neighbors' against the Cisco4 device with use_textfsm=True.

What is the outermost data structure that is returned from 'show lldp
neighbors' (dictionary, list, string, something else)? The Cisco4 device
should only have one LLDP entry (the HPE switch that this router connects
to). From this LLDP data, print out the remote device's interface. In other
words, print out the port number on the HPE switch that Cisco4 connects into.
'''

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
    'host':'cisco4.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_ios',
}

net_connect = ConnectHandler(**device1)
my_cmd1 = "show version"
my_cmd2 = "show lldp neighbors"

my_output1 = net_connect.send_command(my_cmd1, use_textfsm=True)
my_output2 = net_connect.send_command(my_cmd2, use_textfsm=True)

print()
print("Data structure returned from show lldp neighbors is : ", type(my_output2))
print()

print("-" * 80)

print()
# pprint(my_output2)
print("Remote device\'s interface is : ", my_output2[0]['neighbor_interface'])
print()

net_connect.disconnect()

