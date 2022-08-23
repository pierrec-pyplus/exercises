#!/usr/bin/env python

'''
2. PyEZ Tables/Views:

2a. Create a Python module named jnpr_devices.py. This Python module should
contain a dictionary named "srx2". This "srx2" dictionary should contain all of
the key-value pairs needed to establish a PyEZ connection. You should use
getpass() for the password handling. You should import this "srx2" device
definition for all of the remaining exercises in class8.

2b. Create a Python program that creates a PyEZ Device connection to "srx2"
(using the previously created Python module). Using this PyEZ connection and the
RouteTable and ArpTable views retrieve the routing table and the arp table for
srx2.

This program should have four separate functions:
1. check_connected() - Verify that your NETCONF connection is working. You can
use the .connected attribute to check the status of this connection.
2. gather_routes() - Return the routing table from the device.
3. gather_arp_table() - Return the ARP table from the device.
4. print_output() - A function that takes the Juniper PyEZ Device object, the
routing table, and the ARP table and then prints out the: hostname, NETCONF
port, username, routing table, ARP table

This program should be structured such that all of the four functions could be
reused in other class8 exercises.
'''
from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from pprint import pprint

def check_connected(my_jnpr_device):
    return my_jnpr_device.connected

def gather_routes(my_jnpr_device):
    my_routes = RouteTable(my_jnpr_device)
    my_routes.get()
    return my_routes

def gather_arp_table(my_jnpr_device):
    my_arps = ArpTable(my_jnpr_device)
    my_arps.get()
    return my_arps

def print_output(my_jnpr_device, route_table, arp_table):
    # dir(my_jnpr_device)
    print(f"hostname: {my_jnpr_device.hostname}")
    print(f"NETCONF port: {my_jnpr_device.port}")
    print(f"username: {my_jnpr_device.user}")
    print("Route table:")
    pprint(route_table.items())
    print("---")
    print("ARP table:")
    pprint(arp_table.items())


if __name__ == "__main__":
    print()
    print("-" * 80)
    a_device = Device(**srx2)
    a_device.open()
    if check_connected(a_device):
        a_routes = gather_routes(a_device)
        a_arps = gather_arp_table(a_device)
        print_output(a_device, a_routes, a_arps)
    else:
        print(f"Device {a_device.hostname} not connected")
    print("-" * 80)
    print()

