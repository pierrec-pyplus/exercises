#!/usr/bin/env python

'''
2a. Use Python and Jinja2 to generate the below NX-OS interface configuration. You should use an external template file and a Jinja2 environment to accomplish this. The interface, ip_address, and netmask should all be variables in the Jinja2 template.
 
nxos1
interface Ethernet1/1
  ip address 10.1.100.1/24

nxos2
interface Ethernet1/1
  ip address 10.1.100.2/24
'''
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

template_list = [
    {
    "host": "nxos1",
    "vars": {
        "if_name": "Ethernet1/1",
        "ip_addr": "10.1.100.1",
        "mask": 24,
        },
    },
    {
    "host": "nxos2",
    "vars": {
        "if_name": "Ethernet1/1",
        "ip_addr": "10.1.100.2",
        "mask": 24,
        },
    },
]  

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')
template_file = "exercise2a.j2"
template = env.get_template(template_file)

print()
for my_template in template_list:
    print("-" * 80)
    print(my_template["host"]+":")
    output = template.render(**my_template["vars"])
    print(output)
    print("-" * 80)
    print()

