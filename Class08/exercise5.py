#!/usr/bin/env python

'''
5. PYeZ using direct RPC:

5a. Connect to the srx2 device. Using an RPC call, gather and pretty-print the
"show version" information. Recall that you can retrieve RPC method name by
running "show version | display xml rpc" argument. Also don't forget to convert
the hyphens to underscores. Your output should match the following:

<software-information>
<host-name>srx2</host-name>
<product-model>srx110h2-va</product-model>
<product-name>srx110h2-va</product-name>
<jsr/>
<package-information>
<name>junos</name>
<comment>JUNOS Software Release [12.1X46-D35.1]</comment>
</package-information>
</software-information>
'''

from jnpr_devices import srx2
from jnpr.junos import Device
from lxml import etree

print("-" * 80)
print('Exercise 5a: ')
print("-" * 80)

my_device = Device(**srx2)
my_device.open()

# show version
# show version | display xml rpc
# <rpc-reply xmlns:junos="http://xml.juniper.net/junos/12.1X46/junos">
#     <rpc>
#         <get-software-information>
#         </get-software-information>
#     </rpc>
#     <cli>
#         <banner></banner>
#     </cli>
# </rpc-reply>
# get_software_information()
xml_out = my_device.rpc.get_software_information()
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))

print("-" * 80)
input("Press Enter to continue...")
print()

'''
5b. Using a direct RPC call, gather the output of "show interfaces terse". Print
the output to standard out.
'''
print("-" * 80)
print('Exercise 5b: ')
print("-" * 80)

# show interfaces terse | display xml rpc
# <rpc-reply xmlns:junos="http://xml.juniper.net/junos/12.1X46/junos">
#     <rpc>
#         <get-interface-information>
#                 <terse/>
#         </get-interface-information>
#     </rpc>
#     <cli>
#         <banner></banner>
#     </cli>
# </rpc-reply>
# get_interface_information(terse=True)
xml_out = my_device.rpc.get_interface_information(terse=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))

print("-" * 80)
input("Press Enter to continue...")
print()

'''
5c. Modify the previous task to capture "show interface terse", but this time
only for "fe-0/0/7". Print the output to standard out. Use normalize=True in the
RPC method call to make the output more readable. You will also need to add
pretty_print=True to the etree.tostring() call. Consequently, your code should
be similar to the following:

xml_out = dev.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))
'''
print("-" * 80)
print('Exercise 5c: ')
print("-" * 80)

# show interfaces fe-0/0/7 terse | display xml rpc
# <rpc-reply xmlns:junos="http://xml.juniper.net/junos/12.1X46/junos">
#     <rpc>
#         <get-interface-information>
#                 <terse/>
#                 <interface-name>fe-0/0/7</interface-name>
#         </get-interface-information>
#     </rpc>
#     <cli>
#         <banner></banner>
#     </cli>
# </rpc-reply>
# get_interface_information(terse=True, interface_name="fe-0/0/7", normalize=True)
xml_out = my_device.rpc.get_interface_information(terse=True,
                                                  interface_name="fe-0/0/7",
                                                  normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))

print("-" * 80)
print()
