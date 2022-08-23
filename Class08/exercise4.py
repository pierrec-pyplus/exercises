#!/usr/bin/env python

'''
4. PYeZ configuration operations (Part 2):

4a. Using the previously created jnpr_devices.py file, open a connection to srx2
and gather the current routing table information.
'''
from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.utils.config import Config
from exercise2 import gather_routes
from pprint import pprint

print("-" * 80)
print('Exercise 4a: ')
print("-" * 80)

my_device = Device(**srx2)
my_device.open()
my_device.timeout = 60
my_routes = RouteTable(my_device)
my_routes.get()
pprint(my_routes.items())

print("-" * 80)
input("Press Enter to continue...")
print()

'''
4b. Using PyEZ stage a configuration from a file. The file should be "conf"
notation. This configuration should add two static host routes (routed to
discard). These routes should be from the RFC documentation range of 
203.0.113.0/24 (picking any /32 in that range should be fine). Use "merge=True"
for this configuration. For example:
 
routing-options {
    static {
        route 203.0.113.5/32 discard;
        route 203.0.113.200/32 discard;
    }
}
'''
print("-" * 80)
print('Exercise 4b: ')
print("-" * 80)

my_cfg = Config(my_device)
my_cfg.lock()

my_cfg.load(path="jnpr_routes.conf", format="text", merge=True)

print("-" * 80)
input("Press Enter to continue...")
print()

'''
4c. Reusing your gather_routes() function from exercise2, retrieve the routing
table before and after you configuration change. Print out the differences in
the routing table (before and after the change). To simplify the problem, you
can assume that the only change will be *additional* routes added by your
script.
'''
print("-" * 80)
print('Exercise 4c: ')
print("-" * 80)

my_routes = gather_routes(my_device)
pprint(my_routes.items())

my_cfg.commit(comment="Testing from pyez")

my_routes = gather_routes(my_device)
pprint(my_routes.items())

print("-" * 80)
input("Press Enter to continue...")
print()

'''
4d. Using PyEZ delete the static routes that you just added. You can use either
load() and set operations or load() plus a configuration file to accomplish
this.
'''
print("-" * 80)
print('Exercise 4d: ')
print("-" * 80)
my_cfg.load("delete routing-options static route 203.0.113.5/32 discard",
            format="set",
            merge=True
            )
my_cfg.load("delete routing-options static route 203.0.113.200/32 discard",
            format="set",
            merge=True
            )
my_cfg.commit(comment="Testing from pyez")
my_routes = gather_routes(my_device)
pprint(my_routes.items())

print("-" * 80)
print()

my_cfg.unlock()

