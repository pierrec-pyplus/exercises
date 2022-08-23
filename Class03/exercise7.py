#!/usr/bin/env python

'''
You have the following BGP configuration from a Cisco IOS-XR router:

 
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out

From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as. Return a list of tuples. The tuples should be (neighbor_ip, remote_as). Print your data-structure to standard output.

Your output should look similar to the following. Use ciscoconfparse to accomplish this.

 
BGP Peers: 
[('10.220.88.20', '42'), ('10.220.88.32', '43')]
'''

from ciscoconfparse import CiscoConfParse

bgp_conf = """router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out"""

cisco_obj = CiscoConfParse(bgp_conf.splitlines())

match = cisco_obj.find_objects(r"^router bgp 44")
#  for child in match:
bgp_conf = match[0]
bgp_neighbor = bgp_conf.re_search_children(r"^\sneighbor")

my_list =[]

for neighbor in bgp_neighbor:
  nei_list = neighbor.text.split()
  nei_ip = nei_list[1]

  rem_as_list = neighbor.re_search_children(r"remote-as")
  rem_as_string = rem_as_list[0].text
  rem_as = rem_as_string.split()[1]
  my_tuple=(nei_ip, rem_as)
  my_list.append(my_tuple)

print()
print("BGP Peers:")
print(my_list)
print()

