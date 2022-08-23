#!/usr/bin/env python

'''
3a. Create a new function that is a duplicate of your "ssh_command" function.
Name this function "ssh_command2". This function should eliminate all printing
to standard output and should instead return the show command output. Note, in
general, it is problematic to print in the child thread as you can get into
race conditions between the threads. Using the "ThreadPoolExecutor" in 
Concurrent Futures execute "show version" on each of the devices defined in
my_devices.py. Use the 'wait' method to ensure all of the futures have
completed. Concurrent futures should be executing the ssh_command2 function in
the child threads. Print the total execution time required to accomplish this
task.
'''

from my_devices import device_list
from my_functions import ssh_command2
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from datetime import datetime

print("-" * 80)
print('Exercise 3a: ')
print("-" * 80)

start_time = datetime.now()
max_threads = 4
pool = ThreadPoolExecutor(max_threads)
future_list = []

for a_device in device_list:
    future = pool.submit(ssh_command2, a_device, "show version")
    future_list.append(future)

# Waits until all the pending threads are done
wait(future_list)

for future in future_list:
    print("Result: " + future.result())

end_time = datetime.now()
print(end_time - start_time)

print("-" * 80)
input("Press Enter to continue...")
print()

'''
3b. Instead of waiting for all of the futures to complete, use "as_completed"
to print the future results as they come available. Reuse your "ssh_command2"
function to accomplish this. Once again use the concurrent futures
"ThreadPoolExecutor" and print the "show version" results to standard output.
Additionally, print the total execution time to standard output.
'''
print("-" * 80)
print('Exercise 3b: ')
print("-" * 80)

start_time = datetime.now()
max_threads = 4
with ThreadPoolExecutor(max_threads) as pool_b:
    future_list = []
    for a_device in device_list:
        future = pool_b.submit(ssh_command2, a_device, "show version")
        future_list.append(future)

    # Process as completed
    for future in as_completed(future_list):
        print("Result: " + future.result())

end_time = datetime.now()
print(end_time - start_time)

print("-" * 80)
print()

# --------------------------------------------------------------------------------
# Exercise 3a: 
# --------------------------------------------------------------------------------
# Result: Cisco IOS XE Software, Version 16.12.03
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
# cisco3 uptime is 1 week, 6 days, 13 hours, 31 minutes
# Uptime for this control processor is 1 week, 6 days, 13 hours, 32 minutes
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
# Result: Arista vEOS
# Hardware version:    
# Serial number:       
# System MAC address:  00aa.fc05.b513
# 
# Software image version: 4.20.10M
# Architecture:           i386
# Internal build version: 4.20.10M-10040268.42010M
# Internal build ID:      68f3ae78-65cb-4ed3-8675-0ff2219bf118
# 
# Uptime:                 3 weeks, 6 days, 19 hours and 21 minutes
# Total memory:           4010924 kB
# Free memory:            2387536 kB
# 
# Result: Arista vEOS
# Hardware version:    
# Serial number:       
# System MAC address:  00af.fc9a.e49e
# 
# Software image version: 4.20.10M
# Architecture:           i386
# Internal build version: 4.20.10M-10040268.42010M
# Internal build ID:      68f3ae78-65cb-4ed3-8675-0ff2219bf118
# 
# Uptime:                 35 weeks, 0 days, 23 hours and 6 minutes
# Total memory:           4010924 kB
# Free memory:            480360 kB
# 
# Result:  
# Hostname: srx2
# Model: srx110h2-va
# JUNOS Software Release [12.1X46-D35.1]
# 
# 0:00:05.217534
# --------------------------------------------------------------------------------
# Press Enter to continue...
# 
# --------------------------------------------------------------------------------
# Exercise 3b: 
# --------------------------------------------------------------------------------
# Result: Cisco IOS XE Software, Version 16.12.03
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
# cisco3 uptime is 1 week, 6 days, 13 hours, 31 minutes
# Uptime for this control processor is 1 week, 6 days, 13 hours, 33 minutes
# System returned to ROM by Critical software exception, check bootflash:crashinfo_RP_00_00_20220505-170432-PDT at 14:30:28 PST Tue Nov 30 2021
# System restarted at 17:10:11 PDT Thu May 5 2022
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
# Result:  
# Hostname: srx2
# Model: srx110h2-va
# JUNOS Software Release [12.1X46-D35.1]
# 
# Result: Arista vEOS
# Hardware version:    
# Serial number:       
# System MAC address:  00af.fc9a.e49e
# 
# Software image version: 4.20.10M
# Architecture:           i386
# Internal build version: 4.20.10M-10040268.42010M
# Internal build ID:      68f3ae78-65cb-4ed3-8675-0ff2219bf118
# 
# Uptime:                 35 weeks, 0 days, 23 hours and 6 minutes
# Total memory:           4010924 kB
# Free memory:            474300 kB
# 
# Result: Arista vEOS
# Hardware version:    
# Serial number:       
# System MAC address:  00aa.fc05.b513
# 
# Software image version: 4.20.10M
# Architecture:           i386
# Internal build version: 4.20.10M-10040268.42010M
# Internal build ID:      68f3ae78-65cb-4ed3-8675-0ff2219bf118
# 
# Uptime:                 3 weeks, 6 days, 19 hours and 21 minutes
# Total memory:           4010924 kB
# Free memory:            2380168 kB
# 
# 0:00:04.962805
# --------------------------------------------------------------------------------
