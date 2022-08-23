#!/usr/bin/env python

'''
1. Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows:

cisco4#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms

a. Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'

b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'.
'''

from netmiko import ConnectHandler
from getpass import getpass

ios4 = {
    'host':'cisco4.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_ios',
    # 'session_log':'mysession.txt'
}

net_connect = ConnectHandler(**ios4)

command='ping'
my_address='8.8.8.8'

output = net_connect.send_command(command, expect_string=r'Protocol.*:',
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Target IP address:',
    strip_prompt=False, strip_command=False)
output += net_connect.send_command(my_address, expect_string=r'Repeat count.*:',
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Datagram size.*:',
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Timeout in seconds.*:',
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Extended commands.*:',
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Sweep range of sizes.*:',
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'#',
    strip_prompt=False, strip_command=False)

print ("-" * 80)
print(output)
print ("-" * 80)
