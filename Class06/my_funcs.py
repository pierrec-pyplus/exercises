#!/usr/bin/env python

from getpass import getpass
import yaml


def function1(filename):
    with open(filename) as f:
        yaml_out = yaml.safe_load(f)
    passwd = getpass("Password: ")
    for my_dict in yaml_out:
        my_dict.update({"password": passwd})
    return yaml_out

def function2(list):
    print()
    print("-" * 80)
    for my_dict in list[0]['result']['ipV4Neighbors']:
        my_addr = my_dict["address"]
        my_mac = my_dict["hwAddress"]
        print(f'IP addr: {my_addr} - MAC: {my_mac}')
    print("-" * 80)
    print()

