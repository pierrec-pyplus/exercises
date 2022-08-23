#!/usr/bin/env python

'''
4. Replace Operations

4a. Add nxos1 to your my_devices.py file. Ensure that you include the necessary
information to set the NX-API port to 8443. This is done using 'optional_args'
in NAPALM so you should have the following key-value pair defined:
 
"optional_args": {"port": 8443}
'''
from my_devices import nxos1

'''
4b. Create a new function named 'create_checkpoint'. Add this function into your
my_functions.py file. This function should take one argument, the NAPALM
connection object. This function should use the NAPALM _get_checkpoint_file()
method to retrieve a checkpoint from the NX-OS device. It should then write this
checkpoint out to a file.

Recall that the NX-OS platform requires a 'checkpoint' file for configuration
replace operations. Using this new function, retrieve a checkpoint from nxos1
and write it to the local file system.
'''
print("-" * 80)
print('Exercise 4b: ')
print("-" * 80)
print("Create checkpoint")
from my_functions import open_napalm_connection, create_checkpoint
napalm_nxos1 = open_napalm_connection(nxos1)
create_checkpoint(napalm_nxos1)
print("-" * 80)
input("Press Enter to continue...")
print()

'''
4c. Manually copy the saved checkpoint to a new file and add an additional
loopback interface to the configuration.
'''
print("-" * 80)
print('Exercise 4c: ')
print("-" * 80)
print("Manually copy the saved checkpoint to a new file and add an additional loopback interface to the configuration.")
print("-" * 80)
input("Press Enter to continue...")
print()

'''
4d. Create a Python script that stages a complete configuration replace
operation (using the checkpoint file that you just retrieved and modified). Once
your candidate configuration is staged perform a compare_config (diff) on the
configuration to see your pending changes. After the compare_config is complete,
then use the discard_config() method to eliminate the pending changes. Next,
perform an additional compare_config (diff) to verify that you have no pending
configuration changes. Do not actually perform the commit_config as part of this
exercise.
'''
print("-" * 80)
print('Exercise 4d: ')
print("-" * 80)
print("===Load nxos_checkpoint2.cfg===")
napalm_nxos1.load_replace_candidate(filename="nxos1_checkpoint2.cfg")
print("---Display diff---")
print(napalm_nxos1.compare_config())
print("---Display diff---")
print("===DISCARD changes===")
napalm_nxos1.discard_config() 
print("---Display diff---")
print(napalm_nxos1.compare_config())
print("---Display diff---")
print("-" * 80)
print()
napalm_nxos1.close()
