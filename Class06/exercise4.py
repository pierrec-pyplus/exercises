#!/usr/bin/env python

'''
4. Note, this exercise might be fairly challenging. Construct a new YAML file that contains the four Arista switches. This YAML file should contain all of the connection information need to create a pyeapi connection using the connect method. Using this inventory information and pyeapi, create a Python script that configures the following on the four Arista switches: 

interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}
 
The {{ intf_name }} should be a Loopback interface between 1 and 99 (for example Loopback99).

The {{ intf_ip }} should be an address from the 172.31.X.X address space. The {{ intf_mask }} should be either a /24 or a /30.

Each Arista switch should have a unique loopback number, and a unique interface IP address.

You should use Jinja2 templating to generate the configuration for each Arista switch.

The data for {{ intf_name }} and for {{ intf_ip }} should be stored in your YAML file and should be associated with each individual Arista device. For example, here is what 'arista4' might look like in the YAML file:
 
arista4:
  transport: https
  host: arista4.lasthop.io
  username: pyclass
  port: 443
  data:
    intf_name: Loopback99
    intf_ip: 172.31.1.13
    intf_mask: 30

Use pyeapi to push this configuration to the four Arista switches. Use pyeapi and "show ip interface brief" to display the IP address table after the configuration changes have been made.
'''

from my_funcs import function1
from pprint import pprint
from jinja2 import Template
import pyeapi

loopback_config = """interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}"""

# Generate a list of dicts used by pyeapi to connect
device_list = function1("new_device.yml")

for my_device in device_list:
    # use jinja2 yo generate configuration
    template_vars = {
        'intf_name': my_device['data']['intf_name'],
        'intf_ip': my_device['data']['intf_ip'],
        'intf_mask': my_device['data']['intf_mask'],
    }
    j2_template = Template(loopback_config)
    my_config = j2_template.render(**template_vars)

    # use pyeapi to configure arista switch
    # connection
    my_connection = pyeapi.client.connect(**my_device)
    my_arista = pyeapi.client.Node(my_connection)
    # configuration
    my_config_list = my_config.split('\n')
    my_arista.config(my_config_list)
    # verification
    my_output = my_arista.enable("show ip interface brief")
    print()
    print(f"DEVICE: {my_device['host']}")
    for my_line in my_output:
        print(my_line['result']['output'])
    print()
