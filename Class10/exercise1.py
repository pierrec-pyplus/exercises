#!/usr/bin/env python

'''
1a. As you have done in previous classes, create a Python file named 
"my_devices.py". In this file, define the connection information for: 'cisco3',
'arista1', 'arista2', and 'srx2'. This file should contain all the necessary
information to create a Netmiko connection. Use getpass() for the password
handling. Use a global_delay_factor of 4 for both the arista1 device and the
arista2 device. This Python module should be used to store the connection
information for all of the exercises in this lesson.
'''

'''
1b. Create a Python script that executes "show version" on each of the network
devices defined in my_devices.py. This script should execute serially i.e. one
SSH connection after the other. Record the total execution time for the script.
Print the "show version" output and the total execution time to standard output.
As part of this exercise, you should create a function that both establishes a
Netmiko connection and that executes a single show command that you pass in as
argument. This function's arguments should be the Netmiko device dictionary and
the "show-command" argument. The function should return the result from the show
command.
'''

from netmiko import ConnectHandler
from my_devices import device_list
from datetime import datetime

def ssh_command(my_dev, my_sho_command):
    net_connect = ConnectHandler(**my_dev)
    output = net_connect.send_command_expect(my_sho_command)
    return output

start_time = datetime.now()

for a_device in device_list:
    sho_ver = ssh_command(a_device, "show version")
    print("-" * 20)
    print(a_device['host'])
    print(sho_ver)
    print("-" * 20)

print("\nElapsed time: " + str(datetime.now() - start_time))

# --------------------
# cisco3.lasthop.io
# 
# Cisco IOS XE Software, Version 16.12.03
# Cisco IOS Software [Gibraltar], ISR Software (ARMV8EL_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.12.3, RELEASE SOFTWARE (fc5)
# Technical Support: http://www.cisco.com/techsupport
# Copyright (c) 1986-2020 by Cisco Systems, Inc.
# Compiled Mon 09-Mar-20 20:31 by mcpre
# 
# 
# Cisco IOS-XE software, Copyright (c) 2005-2020 by cisco Systems, Inc.
# All rights reserved.  Certain components of Cisco IOS-XE software are
# licensed under the GNU General Public License ("GPL") Version 2.0.  The
# software code licensed under GPL Version 2.0 is free software that comes
# with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
# GPL code under the terms of GPL Version 2.0.  For more details, see the
# documentation or "License Notice" file accompanying the IOS-XE software,
# or the applicable URL provided on the flyer accompanying the IOS-XE
# software.
# 
# 
# ROM: IOS-XE ROMMON
# 
# cisco3 uptime is 1 week, 6 days, 10 hours, 35 minutes
# Uptime for this control processor is 1 week, 6 days, 10 hours, 36 minutes
# System returned to ROM by Critical software exception, check bootflash:crashinfo_RP_00_00_20220505-170432-PDT at 14:30:28 PST Tue Nov 30 2021
# System restarted at 17:10:12 PDT Thu May 5 2022
# System image file is "bootflash:c1100-universalk9_ias.16.12.03.SPA.bin"
# Last reload reason: Critical software exception, check bootflash:crashinfo_RP_00_00_20220505-170432-PDT
# 
# 
# 
# This product contains cryptographic features and is subject to United
# States and local country laws governing import, export, transfer and
# use. Delivery of Cisco cryptographic products does not imply
# third-party authority to import, export, distribute or use encryption.
# Importers, exporters, distributors and users are responsible for
# compliance with U.S. and local country laws. By using this product you
# agree to comply with applicable laws and regulations. If you are unable
# to comply with U.S. and local laws, return this product immediately.
# 
# A summary of U.S. laws governing Cisco cryptographic products may be found at:
# http://www.cisco.com/wwl/export/crypto/tool/stqrg.html
# 
# If you require further assistance please contact us by sending email to
# export@cisco.com.
# 
# 
# 
# Suite License Information for Module:'esg' 
# 
# --------------------------------------------------------------------------------
# Suite                 Suite Current         Type           Suite Next reboot     
# --------------------------------------------------------------------------------
# FoundationSuiteK9     None                  Smart License  None                  
# securityk9
# appxk9
# 
# 
# Technology Package License Information: 
# 
# -----------------------------------------------------------------
# Technology    Technology-package           Technology-package
#               Current       Type           Next reboot  
# ------------------------------------------------------------------
# appxk9           None             Smart License    None
# securityk9       None             Smart License    None
# ipbase           ipbasek9         Smart License    ipbasek9
# 
# The current throughput level is unthrottled 
# 
# 
# Smart Licensing Status: REGISTERED/AUTHORIZED
# 
# cisco C1111-4P (1RU) processor with 1401823K/6147K bytes of memory.
# Processor board ID FGL222290LB
# 1 Virtual Ethernet interface
# 6 Gigabit Ethernet interfaces
# 32768K bytes of non-volatile configuration memory.
# 4194304K bytes of physical memory.
# 2863103K bytes of flash memory at bootflash:.
# 0K bytes of WebUI ODM Files at webui:.
# 
# Configuration register is 0x2102
# 
# --------------------
# --------------------
# arista1.lasthop.io
# Arista vEOS
# Hardware version:    
# Serial number:       
# System MAC address:  00aa.fc05.b513
# 
# Software image version: 4.20.10M
# Architecture:           i386
# Internal build version: 4.20.10M-10040268.42010M
# Internal build ID:      68f3ae78-65cb-4ed3-8675-0ff2219bf118
# 
# Uptime:                 3 weeks, 6 days, 16 hours and 25 minutes
# Total memory:           4010924 kB
# Free memory:            2391968 kB
# 
# --------------------
# --------------------
# arista2.lasthop.io
# Arista vEOS
# Hardware version:    
# Serial number:       
# System MAC address:  00af.fc9a.e49e
# 
# Software image version: 4.20.10M
# Architecture:           i386
# Internal build version: 4.20.10M-10040268.42010M
# Internal build ID:      68f3ae78-65cb-4ed3-8675-0ff2219bf118
# 
# Uptime:                 35 weeks, 0 days, 20 hours and 10 minutes
# Total memory:           4010924 kB
# Free memory:            484068 kB
# 
# --------------------
# --------------------
# srx2.lasthop.io
#  
# Hostname: srx2
# Model: srx110h2-va
# JUNOS Software Release [12.1X46-D35.1]
# 
# --------------------
# 
# Elapsed time: 0:00:13.348661
