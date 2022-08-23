#!/usr/bin/env python

'''
Using the below ARP data, create a five element list. Each list element should be a dictionary with the following keys: "mac_addr", "ip_addr", "interface". At the end of this process, you should have five dictionaries contained inside a single list.

 
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

from pprint import pprint

my_arp = '''Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0'''

# strip multiline variable into lines
my_arp_lines = my_arp.split('\n')

# separate keys from values
my_arp_keys = my_arp_lines.pop(0)

# separate keys in list
my_arp_keys = my_arp_keys.split()
# pprint(my_arp_keys)
# pprint(my_arp_lines)

new_list = []
for my_lines in my_arp_lines:
    pprint(my_lines)
    my_lines = my_lines.split()
    new_entry = {
        "mac_addr": my_lines[3],
        "ip_addr": my_lines[1],
        "interface": my_lines[5],
    }
    new_list.append(new_entry)

print()
pprint(new_list)
print()
