#!/usr/bin/env python

'''
4. Expand on exercise3 except use a for-loop to configure five VRFs. Each VRF should have a unique name and a unique route distinguisher. Each VRF should once again have the IPv4 and the IPv6 address families controlled by a conditional-variable passed into the template.

Note, you will want to pass in a list or dictionary of VRFs that you loop over in your Jinja2 template.
'''

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')

vrf1 = {"vrf_name": "blue", "rd_number": "100:1", "ipv4": True, "ipv6": True}
vrf2 = {"vrf_name": "red", "rd_number": "100:2", "ipv4": False, "ipv6": True}
vrf3 = {"vrf_name": "orange", "rd_number": "100:3", "ipv4": True, "ipv6": False}
vrf4 = {"vrf_name": "green", "rd_number": "100:4", "ipv4": False, "ipv6": False}
vrf5 = {"vrf_name": "purple", "rd_number": "100:5", "ipv4": True, "ipv6": True}

vrf_vars = { "vrf_list": [ vrf1, vrf2, vrf3, vrf4, vrf5 ] }

template_file = "exercise4.j2"
template = env.get_template(template_file)
output = template.render(**vrf_vars)
print()
print("-" * 80)
print(output)
print("-" * 80)
print()

