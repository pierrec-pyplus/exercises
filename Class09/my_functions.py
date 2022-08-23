#!/usr/bin/env python
from napalm import get_network_driver

def open_napalm_connection(my_device):
    device_type = my_device.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**my_device)
    print(f"opening connection to {my_device['hostname']}")
    device.open()
    return device

def create_backup(napalm_conn_obj):
    my_running_config = napalm_conn_obj.get_config()['running']
    my_filename = napalm_conn_obj.get_facts()['hostname'] + ".cfg"
    f = open(my_filename, "w")
    f.write(my_running_config)
    f.close()

def create_checkpoint(napalm_conn_obj):
    my_checkpoint = napalm_conn_obj._get_checkpoint_file()
    my_filename = napalm_conn_obj.get_facts()['hostname'] + "_checkpoint.cfg"
    f = open(my_filename, "w")
    f.write(my_checkpoint)
    f.close()

