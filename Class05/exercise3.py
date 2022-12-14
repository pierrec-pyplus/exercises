#!/usr/bin/env python

'''
3. Generate the following configuration output from an external Jinja2 template:

vrf definition blue
rd 100:1
!
address-family ipv4
  route-target export 100:1
  route-target import 100:1
exit-address-family
!
address-family ipv6
  route-target export 100:1
  route-target import 100:1
exit-address-family

Both the IPv4 and the IPv6 address families should be controlled by Jinja2 conditionals (in other words, the entire 'address-family ipv4' section and the entire 'address-family ipv6' sections can be dropped from the generated output depending on the value of two variables that you pass into your template--for example, the 'ipv4_enabled' and the 'ipv6_enabled' variables). Additionally, both the vrf_name and the rd_number should be variables in the template. Make sure that you control the whitespace in your output such that the configuration looks visually correct.
'''

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')

vrf_vars = {"vrf_name": "blue", "rd_number": "100:1", "ipv4": True, "ipv6": True}
# vrf_vars = {"vrf_name": "blue", "rd_number": "100:1", "ipv4": True, "ipv6": False}
# vrf_vars = {"vrf_name": "blue", "rd_number": "100:1", "ipv4": False, "ipv6": True}
# vrf_vars = {"vrf_name": "blue", "rd_number": "100:1", "ipv4": False, "ipv6": False}

template_file = "exercise3.j2"
template = env.get_template(template_file)
output = template.render(**vrf_vars)
print()
print("-" * 80)
print(output)
print("-" * 80)
print()

