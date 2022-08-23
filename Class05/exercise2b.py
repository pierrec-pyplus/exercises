#!/usr/bin/env python

'''
2b. Expand your Jinja2 template such that both the following interface and BGP configurations are generated for nxos1 and nxos2. The interface name, IP address, netmask, local_as, and peer_ip should all be variables in the template. This is iBGP so the remote_as will be the same as the local_as.

nxos1

interface Ethernet1/1
  ip address 10.1.100.1/24

router bgp 22
  neighbor 10.1.100.2 remote-as 22
    address-family ipv4 unicast

nxos2
interface Ethernet1/1
  ip address 10.1.100.2/24

router bgp 22
  neighbor 10.1.100.1 remote-as 22
    address-family ipv4 unicast
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
        "local_as": 22,
        "peer_ip": "10.1.100.2",
        },
    },  
    {   
    "host": "nxos2",
    "vars": {
        "if_name": "Ethernet1/1",
        "ip_addr": "10.1.100.2",
        "mask": 24, 
        "local_as": 22,
        "peer_ip": "10.1.100.1",
        },
    },  
]  
 
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')
template_file = "exercise2b.j2"
template = env.get_template(template_file)
 
print()
for my_template in template_list:
    print("-" * 80) 
    print(my_template["host"]+":")
    output = template.render(**my_template["vars"])
    print(output)
    print("-" * 80) 
    print()

