#!/usr/bin/env python

'''
6. NX-API using json-rpc and the nxapi_plumbing library

6a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be
"jsonrpc" and the transport should be "https" (port 8443). Use getpass() to
capture the device's password. Send the "show interface Ethernet1/1" command to
the device, parse the output, and print out the following information:
 
Interface: Ethernet1/1; State: up; MTU: 1500
'''

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")

#{'TABLE_interface': {'ROW_interface': {'admin_state': 'up',
#                                       'encapsulation': 'ARPA',
#                                       'eth_autoneg': 'on',
#                                       'eth_babbles': '0',
#                                       'eth_bad_eth': '0',
#                                       'eth_bad_proto': '0',
#                                       'eth_beacon': 'off',
#                                       'eth_bia_addr': '5254.0012.345e',
#                                       'eth_bw': 1000000,
#                                       'eth_clear_counters': 'never',
#                                       'eth_coll': '0',
#                                       'eth_crc': '0',
#                                       'eth_deferred': '0',
#                                       'eth_dly': 10,
#                                       'eth_dribble': '0',
#                                       'eth_duplex': 'full',
#                                       'eth_eee_state': 'n/a',
#                                       'eth_ethertype': '0x8100',
#                                       'eth_frame': '0',
#                                       'eth_giants': 0,
#                                       'eth_hw_addr': '000c.29d1.0001',
#                                       'eth_hw_desc': '100/1000/10000 Ethernet',
#                                       'eth_ignored': '0',
#                                       'eth_in_flowctrl': 'off',
#                                       'eth_in_ifdown_drops': '0',
#                                       'eth_inbcast': 0,
#                                       'eth_inbytes': 0,
#                                       'eth_indiscard': '0',
#                                       'eth_inerr': '0',
#                                       'eth_inmcast': 0,
#                                       'eth_inpause': '0',
#                                       'eth_inpkts': 0,
#                                       'eth_inrate1_bits': '0',
#                                       'eth_inrate1_pkts': '0',
#                                       'eth_inrate1_summary_bits': '0 bps',
#                                       'eth_inrate1_summary_pkts': '0 pps',
#                                       'eth_inrate2_bits': '0',
#                                       'eth_inrate2_pkts': '0',
#                                       'eth_inrate2_summary_bits': '0 bps',
#                                       'eth_inrate2_summary_pkts': '0 pps',
#                                       'eth_inucast': 0,
#                                       'eth_jumbo_inpkts': '0',
#                                       'eth_jumbo_outpkts': '0',
#                                       'eth_latecoll': '0',
#                                       'eth_link_flapped': '3week(s) 1day(s)',
#                                       'eth_load_interval1_rx': 30,
#                                       'eth_load_interval1_tx': '30',
#                                       'eth_load_interval2_rx': '300',
#                                       'eth_load_interval2_tx': '300',
#                                       'eth_lostcarrier': '0',
#                                       'eth_mdix': 'off',
#                                       'eth_mtu': '1500',
#                                       'eth_nobuf': 0,
#                                       'eth_nocarrier': '0',
#                                       'eth_out_flowctrl': 'off',
#                                       'eth_outbcast': 0,
#                                       'eth_outbytes': 0,
#                                       'eth_outdiscard': '0',
#                                       'eth_outerr': '0',
#                                       'eth_outmcast': 0,
#                                       'eth_outpause': '0',
#                                       'eth_outpkts': 0,
#                                       'eth_outrate1_bits': '0',
#                                       'eth_outrate1_pkts': '0',
#                                       'eth_outrate1_summary_bits': '0 bps',
#                                       'eth_outrate1_summary_pkts': '0 pps',
#                                       'eth_outrate2_bits': '0',
#                                       'eth_outrate2_pkts': '0',
#                                       'eth_outrate2_summary_bits': '0 bps',
#                                       'eth_outrate2_summary_pkts': '0 pps',
#                                       'eth_outucast': 0,
#                                       'eth_overrun': '0',
#                                       'eth_reliability': '255',
#                                       'eth_reset_cntr': 3,
#                                       'eth_runts': 0,
#                                       'eth_rxload': '1',
#                                       'eth_speed': '1000 Mb/s',
#                                       'eth_storm_supp': '0',
#                                       'eth_swt_monitor': 'off',
#                                       'eth_txload': '1',
#                                       'eth_underrun': '0',
#                                       'eth_watchdog': '0',
#                                       'interface': 'Ethernet1/1',
#                                       'medium': 'broadcast',
#                                       'share_state': 'Dedicated',
#                                       'state': 'up'}}}

output = output["TABLE_interface"]["ROW_interface"]

print(f"Interface: {output['interface']}; State: {output['state']}; MTU: {output['eth_mtu']}")

