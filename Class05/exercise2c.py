#!/usr/bin/env python

'''
2c. Use Netmiko to push the configurations generated in exercise 2b to the nxos1 device and to the nxos2 device, respectively. Verify you are able to ping between the devices and also verify that the BGP session reaches the established state. Note, you might need to use an alternate interface besides Ethernet 1/1 (you can use either Ethernet 1/1, 1/2, 1/3, or 1/4). Additionally, you might need to use a different IP network (to avoid conflicts with other students). Your autonomous system should remain 22, however.

For this exercise you should store your Netmiko connection dictionaries in an external file named my_devices.py and should import nxos1, and nxos2 from that external file. Make sure that you use getpass() to enter the password in for these devices (as opposed to storing the definitions in the file).

Note, this exercise gets a bit complicated when it is all said and done (templating, pushing configuration to devices, verifying the changes were successful).
'''
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from my_devices import nxos1, nxos2 
from netmiko import ConnectHandler
from pprint import pprint

nxos1_template_vars = {
        "if_name": "Ethernet1/1",
        "ip_addr": "10.1.100.1",
        "mask": 24, 
        "local_as": 22, 
        "peer_ip": "10.1.100.2",
}  
nxos2_template_vars = {
        "if_name": "Ethernet1/1",
        "ip_addr": "10.1.100.2",
        "mask": 24, 
        "local_as": 22, 
        "peer_ip": "10.1.100.1",
}  

my_list = [
    { "host": nxos1, "template": nxos1_template_vars},
    { "host": nxos2, "template": nxos2_template_vars},
 ]

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')
template_file = "exercise2c.j2"
template = env.get_template(template_file)

## configuring 
for my_elements in my_list:
    print("configuring host : "+my_elements["host"]["host"])
    my_config = template.render(**my_elements["template"])
    my_connect = ConnectHandler(**my_elements["host"])
    my_config_list = my_config.splitlines()
    output = my_connect.send_config_set(my_config_list)

## verifying
print()
for my_elements in my_list:
    print("-" * 80)
    print("Host is : "+my_elements["host"]["host"])
    my_connect = ConnectHandler(**my_elements["host"])
    output = my_connect.send_command("ping "+my_elements["template"]["peer_ip"])
    print(output)
    output = my_connect.send_command("sho ip bgp summary  | include ^Neighbor|^"+my_elements["template"]["peer_ip"])
    print(output)
    print("-" * 80)
    print()

