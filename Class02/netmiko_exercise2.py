#!/usr/bin/env python

'''
Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. Execute 'show lldp neighbors detail' and print the returned output to standard output. Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. Print the output of this command to standard output. Use the Python datetime library to record the execution time of both of these commands. Print these execution times to standard output.
'''

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = { 
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_ios',
    'global_delay_factor': 2,
}
my_command = "show lldp neighbors detail"
net_connect = ConnectHandler(**device1)
# print(net_connect.find_prompt())

print("-" * 80)
start_time = datetime.now()
output = net_connect.send_command(my_command)
end_time = datetime.now()
delay = end_time - start_time
print("delay in sec = ",  delay.total_seconds())
# print(output)
print("-" * 80)

print("=" * 80)
start_time = datetime.now()
output = net_connect.send_command(my_command, delay_factor=8)
end_time = datetime.now()
delay = end_time - start_time
print("delay in sec = ",  delay.total_seconds())
# print(output)
print("=" * 80)

