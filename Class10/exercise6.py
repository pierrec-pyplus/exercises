#!/usr/bin/env python

'''
6. Using a context manager, the ProcessPoolExecutor, and the map() method,
create a solution that executes "show ip arp" on all of the devices defined in
my_devices.py. Note, the Juniper device will require "show arp" instead of
"show ip arp" so your solution will have to properly account for this.
'''

from my_devices import device_list
from my_functions import ssh_command2
from concurrent.futures import ProcessPoolExecutor
 

# Build cmd list
cmd_list = []
for device in device_list:
    if device['device_type'] == 'juniper_junos':
        cmd = "show arp"
    else:
        cmd = "sho ip arp"
    cmd_list.append(cmd)

max_procs = 4 
with ProcessPoolExecutor(max_procs) as pool:
    results_generator = pool.map(ssh_command2, device_list, cmd_list) 

    # Results generator
    for result in results_generator:
        print(result)
        print("-" * 80)

# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.220.88.1            32   0024.c4e9.48ae  ARPA   GigabitEthernet0/0/0
# Internet  10.220.88.21          177   1c6a.7aaf.576c  ARPA   GigabitEthernet0/0/0
# Internet  10.220.88.22            -   a093.5141.b780  ARPA   GigabitEthernet0/0/0
# Internet  10.220.88.28          208   00aa.fc05.b513  ARPA   GigabitEthernet0/0/0
# Internet  10.220.88.31          118   00ac.fc59.97f2  ARPA   GigabitEthernet0/0/0
# Internet  10.220.88.37          112   0001.00ff.0001  ARPA   GigabitEthernet0/0/0
# Internet  10.220.88.38          169   0002.00ff.0001  ARPA   GigabitEthernet0/0/0
# --------------------------------------------------------------------------------
# Address         Age (min)  Hardware Addr   Interface
# 10.220.88.1           N/A  0024.c4e9.48ae  Vlan1, Ethernet1
# 10.220.88.20          N/A  c89c.1dea.0eb6  Vlan1, not learned
# 10.220.88.22          N/A  a093.5141.b780  Vlan1, not learned
# 10.220.88.29          N/A  00af.fc9a.e49e  Vlan1, not learned
# 10.220.88.30          N/A  00ab.fcc0.f97c  Vlan1, not learned
# 10.220.88.31          N/A  00ac.fc59.97f2  Vlan1, not learned
# 10.220.88.37          N/A  0001.00ff.0001  Vlan1, not learned
# 10.220.88.38          N/A  0002.00ff.0001  Vlan1, not learned
# --------------------------------------------------------------------------------
# Address         Age (min)  Hardware Addr   Interface
# 10.220.88.1           N/A  0024.c4e9.48ae  Vlan1, Ethernet1
# 10.220.88.28          N/A  00aa.fc05.b513  Vlan1, not learned
# 10.220.88.30          N/A  00ab.fcc0.f97c  Vlan1, not learned
# 10.220.88.31          N/A  00ac.fc59.97f2  Vlan1, not learned
# 10.220.88.37          N/A  0001.00ff.0001  Vlan1, not learned
# 10.220.88.38          N/A  0002.00ff.0001  Vlan1, not learned
# --------------------------------------------------------------------------------
#  
# MAC Address       Address         Name                      Interface           Flags
# 00:24:c4:e9:48:ae 10.220.88.1     10.220.88.1               vlan.0              none
# 00:01:00:ff:00:01 10.220.88.37    10.220.88.37              vlan.0              none
# 00:02:00:ff:00:01 10.220.88.38    10.220.88.38              vlan.0              none
# Total entries: 3
# 
# --------------------------------------------------------------------------------
