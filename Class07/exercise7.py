#!/usr/bin/env python

'''
7. NX-API using XML and the nxapi_plumbing library
'''

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

'''
7a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be
"xml" and the transport should be "https" (port 8443). Use getpass() to capture
the device's password. Send the "show interface Ethernet1/1" command to the
device, parse the output, and print out the following information:
 
Interface: Ethernet1/1; State: up; MTU: 1500
'''
print("-" * 80)
print('Exercise 7a: ')
print("-" * 80)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")

#print(etree.tostring(output).decode())
#<output>
#      <body>
#        <TABLE_interface>
#         <ROW_interface>
#          <interface>Ethernet1/1</interface>
#          <state>up</state>
#          <admin_state>up</admin_state>
#          <share_state>Dedicated</share_state>
#          <eth_hw_desc>100/1000/10000 Ethernet</eth_hw_desc>
#          <eth_hw_addr>000c.29d1.0001</eth_hw_addr>
#          <eth_bia_addr>5254.0012.345e</eth_bia_addr>
#          <eth_mtu>1500</eth_mtu>
#          <eth_bw>1000000</eth_bw>
#          <eth_dly>10</eth_dly>
#          <eth_reliability>255</eth_reliability>
#          <eth_txload>1</eth_txload>
#          <eth_rxload>1</eth_rxload>
#          <encapsulation>ARPA</encapsulation>
#          <medium>broadcast</medium>
#          <eth_duplex>full</eth_duplex>
#          <eth_speed>1000 Mb/s</eth_speed>
#          <eth_beacon>off</eth_beacon>
#          <eth_autoneg>on</eth_autoneg>
#          <eth_in_flowctrl>off</eth_in_flowctrl>
#          <eth_out_flowctrl>off</eth_out_flowctrl>
#          <eth_mdix>off</eth_mdix>
#          <eth_swt_monitor>off</eth_swt_monitor>
#          <eth_ethertype>0x8100</eth_ethertype>
#          <eth_eee_state>n/a</eth_eee_state>
#          <eth_link_flapped>3week(s) 1day(s)</eth_link_flapped>
#          <eth_clear_counters>never</eth_clear_counters>
#          <eth_reset_cntr>3</eth_reset_cntr>
#          <eth_load_interval1_rx>30</eth_load_interval1_rx>
#          <eth_inrate1_bits>0</eth_inrate1_bits>
#          <eth_inrate1_pkts>0</eth_inrate1_pkts>
#          <eth_load_interval1_tx>30</eth_load_interval1_tx>
#          <eth_outrate1_bits>0</eth_outrate1_bits>
#          <eth_outrate1_pkts>0</eth_outrate1_pkts>
#          <eth_inrate1_summary_bits>0 bps</eth_inrate1_summary_bits>
#          <eth_inrate1_summary_pkts>0 pps</eth_inrate1_summary_pkts>
#          <eth_outrate1_summary_bits>0 bps</eth_outrate1_summary_bits>
#          <eth_outrate1_summary_pkts>0 pps</eth_outrate1_summary_pkts>
#          <eth_load_interval2_rx>300</eth_load_interval2_rx>
#          <eth_inrate2_bits>0</eth_inrate2_bits>
#          <eth_inrate2_pkts>0</eth_inrate2_pkts>
#          <eth_load_interval2_tx>300</eth_load_interval2_tx>
#          <eth_outrate2_bits>0</eth_outrate2_bits>
#          <eth_outrate2_pkts>0</eth_outrate2_pkts>
#          <eth_inrate2_summary_bits>0 bps</eth_inrate2_summary_bits>
#          <eth_inrate2_summary_pkts>0 pps</eth_inrate2_summary_pkts>
#          <eth_outrate2_summary_bits>0 bps</eth_outrate2_summary_bits>
#          <eth_outrate2_summary_pkts>0 pps</eth_outrate2_summary_pkts>
#          <eth_inucast>0</eth_inucast>
#          <eth_inmcast>0</eth_inmcast>
#          <eth_inbcast>0</eth_inbcast>
#          <eth_inpkts>0</eth_inpkts>
#          <eth_inbytes>0</eth_inbytes>
#          <eth_jumbo_inpkts>0</eth_jumbo_inpkts>
#          <eth_storm_supp>0</eth_storm_supp>
#          <eth_runts>0</eth_runts>
#          <eth_giants>0</eth_giants>
#          <eth_crc>0</eth_crc>
#          <eth_nobuf>0</eth_nobuf>
#          <eth_inerr>0</eth_inerr>
#          <eth_frame>0</eth_frame>
#          <eth_overrun>0</eth_overrun>
#          <eth_underrun>0</eth_underrun>
#          <eth_ignored>0</eth_ignored>
#          <eth_watchdog>0</eth_watchdog>
#          <eth_bad_eth>0</eth_bad_eth>
#          <eth_bad_proto>0</eth_bad_proto>
#          <eth_in_ifdown_drops>0</eth_in_ifdown_drops>
#          <eth_dribble>0</eth_dribble>
#          <eth_indiscard>0</eth_indiscard>
#          <eth_inpause>0</eth_inpause>
#          <eth_outucast>0</eth_outucast>
#          <eth_outmcast>0</eth_outmcast>
#          <eth_outbcast>0</eth_outbcast>
#          <eth_outpkts>0</eth_outpkts>
#          <eth_outbytes>0</eth_outbytes>
#          <eth_jumbo_outpkts>0</eth_jumbo_outpkts>
#          <eth_outerr>0</eth_outerr>
#          <eth_coll>0</eth_coll>
#          <eth_deferred>0</eth_deferred>
#          <eth_latecoll>0</eth_latecoll>
#          <eth_lostcarrier>0</eth_lostcarrier>
#          <eth_nocarrier>0</eth_nocarrier>
#          <eth_babbles>0</eth_babbles>
#          <eth_outdiscard>0</eth_outdiscard>
#          <eth_outpause>0</eth_outpause>
#         </ROW_interface>
#        </TABLE_interface>
#       </body>
#      <input>show interface Ethernet1/1</input>
#      <msg>Success</msg>
#      <code>200</code>
#    </output>

ifname = output.find(".//interface").text
ifstate = output.find(".//state").text
ifmtu = output.find(".//eth_mtu").text

print(f"Interface: {ifname}; State: {ifstate}; MTU: {ifmtu}")

print("-" * 80)
input("Press a key to continue...")
print()

'''
7b. Run the following two show commands on the nxos1 device using a single
method and passing in a list of commands: "show system uptime" and "show system
resources". Print the XML output from these two commands.
'''
print("-" * 80)
print('Exercise 7b: ')
print("-" * 80)

cmds = ["show system uptime", "show system resources"]
output = device.show_list(cmds)
for entry in output:
    print(etree.tostring(entry).decode())
    input("Hit enter to continue: ")

#<output>
#      <body>
#       <sys_st_time>Tue Apr  6 21:24:40 2021</sys_st_time>
#       <sys_up_days>387</sys_up_days>
#       <sys_up_hrs>16</sys_up_hrs>
#       <sys_up_mins>51</sys_up_mins>
#       <sys_up_secs>6</sys_up_secs>
#       <kn_up_days>387</kn_up_days>
#       <kn_up_hrs>16</kn_up_hrs>
#       <kn_up_mins>53</kn_up_mins>
#       <kn_up_secs>42</kn_up_secs>
#      </body>
#      <input>show system uptime</input>
#      <msg>Success</msg>
#      <code>200</code>
#    </output>
#    
#Hit enter to continue: 
#<output>
#      <body>
#       <load_avg_1min>3.70</load_avg_1min>
#       <load_avg_5min>3.23</load_avg_5min>
#       <load_avg_15min>3.13</load_avg_15min>
#       <processes_total>639</processes_total>
#       <processes_running>9</processes_running>
#       <cpu_state_user>13.60</cpu_state_user>
#       <cpu_state_kernel>33.72</cpu_state_kernel>
#       <cpu_state_idle>52.66</cpu_state_idle>
#       <TABLE_cpu_usage>
#        <ROW_cpu_usage>
#         <cpuid>0</cpuid>
#         <user>24.39</user>
#         <kernel>30.48</kernel>
#         <idle>45.12</idle>
#        </ROW_cpu_usage>
#        <ROW_cpu_usage>
#         <cpuid>1</cpuid>
#         <user>3.48</user>
#         <kernel>38.37</kernel>
#         <idle>58.13</idle>
#        </ROW_cpu_usage>
#       </TABLE_cpu_usage>
#       <memory_usage_total>6096260</memory_usage_total>
#       <memory_usage_used>4527400</memory_usage_used>
#       <memory_usage_free>1568860</memory_usage_free>
#       <current_memory_status>OK</current_memory_status>
#      </body>
#      <input>show system resources</input>
#      <msg>Success</msg>
#      <code>200</code>
#    </output>
#Hit enter to continue: 

print("-" * 80)
input("Press a key to continue...")
print()

'''
7c. Using the nxapi_plumbing config_list() method, configure two loopbacks on
nxos1 including interface descriptions. Pick random loopback interface numbers
between 100 and 199.
'''
print("-" * 80)
print('Exercise 7c: ')
print("-" * 80)

cfg_cmd = ["interface loopback 176","description my_loopback_176", "interface loopback 179","description my_loopback_179"]
output = device.config_list(cfg_cmd)

for result in output:
    print(etree.tostring(result).decode())

print("-" * 80)
print()

# output
#(py3_venv) [cucurullo@pylab28a Class07]$ ./exercise7.py 
#--------------------------------------------------------------------------------
#Exercise 7a: 
#--------------------------------------------------------------------------------
#Password: 
#Interface: Ethernet1/1; State: up; MTU: 1500
#--------------------------------------------------------------------------------
#Press a key to continue...
#
#--------------------------------------------------------------------------------
#Exercise 7b: 
#--------------------------------------------------------------------------------
#<output>
#      <body>
#       <sys_st_time>Tue Apr  6 21:24:40 2021</sys_st_time>
#       <sys_up_days>387</sys_up_days>
#       <sys_up_hrs>17</sys_up_hrs>
#       <sys_up_mins>5</sys_up_mins>
#       <sys_up_secs>8</sys_up_secs>
#       <kn_up_days>387</kn_up_days>
#       <kn_up_hrs>17</kn_up_hrs>
#       <kn_up_mins>7</kn_up_mins>
#       <kn_up_secs>43</kn_up_secs>
#      </body>
#      <input>show system uptime</input>
#      <msg>Success</msg>
#      <code>200</code>
#    </output>
#    
#Hit enter to continue: 
#<output>
#      <body>
#       <load_avg_1min>2.84</load_avg_1min>
#       <load_avg_5min>2.99</load_avg_5min>
#       <load_avg_15min>2.99</load_avg_15min>
#       <processes_total>639</processes_total>
#       <processes_running>6</processes_running>
#       <cpu_state_user>6.74</cpu_state_user>
#       <cpu_state_kernel>35.95</cpu_state_kernel>
#       <cpu_state_idle>57.30</cpu_state_idle>
#       <TABLE_cpu_usage>
#        <ROW_cpu_usage>
#         <cpuid>0</cpuid>
#         <user>5.68</user>
#         <kernel>6.81</kernel>
#         <idle>87.50</idle>
#        </ROW_cpu_usage>
#        <ROW_cpu_usage>
#         <cpuid>1</cpuid>
#         <user>8.79</user>
#         <kernel>64.83</kernel>
#         <idle>26.37</idle>
#        </ROW_cpu_usage>
#       </TABLE_cpu_usage>
#       <memory_usage_total>6096260</memory_usage_total>
#       <memory_usage_used>4529772</memory_usage_used>
#       <memory_usage_free>1566488</memory_usage_free>
#       <current_memory_status>OK</current_memory_status>
#      </body>
#      <input>show system resources</input>
#      <msg>Success</msg>
#      <code>200</code>
#    </output>
#  
#Hit enter to continue: 
#--------------------------------------------------------------------------------
#Press a key to continue...
#
#--------------------------------------------------------------------------------
#Exercise 7c: 
#--------------------------------------------------------------------------------
#<output>
#      <body/>
#      <code>200</code>
#      <msg>Success</msg>
#    </output>
#    
#<output>
#      <body/>
#      <code>200</code>
#      <msg>Success</msg>
#    </output>
#    
#<output>
#      <body/>
#      <code>200</code>
#      <msg>Success</msg>
#    </output>
#    
#<output>
#      <body/>
#      <code>200</code>
#      <msg>Success</msg>
#    </output>
#  
#--------------------------------------------------------------------------------
#
#
