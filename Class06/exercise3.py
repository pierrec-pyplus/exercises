#!/usr/bin/env python

'''
3. Using your external YAML file and your function located in my_funcs.py, use pyeapi to connect to arista4.lasthop.io and retrieve "show ip route". From this routing table data, extract all of the static and connected routes from the default VRF. Print these routes to the screen and indicate whether the route is a connected route or a static route. In the case of a static route, print the next hop address.
'''

from my_funcs import function1
import pyeapi

device_list = function1("my_device.yml")

for device_dict in device_list:
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip route")

for my_result in output:
    routes_list = my_result['result']['vrfs']['default']['routes']
    print()
    print("-" * 80)
    for k, v in routes_list.items():
        if v['routeType'] == 'static':
            my_NHR_list = []
            for NHR in v['vias']:
                my_NHR_list.append(NHR['nexthopAddr'])
#           print(f'STATIC: {k} NHR: {my_NHR_list}')
            my_NHR_string = ' '.join(my_NHR_list)
            print(f'STATIC: {k} NHR: {my_NHR_string}')
        elif v['routeType'] == 'connected':
            print(f'CONNECTED: {k}')
    print("-" * 80)
    print()
    



# [{'command': 'show ip route',
#   'encoding': 'json',
#   'result': {'vrfs': {'default': {'allRoutesProgrammedHardware': True,
#                                   'allRoutesProgrammedKernel': True,
#                                   'defaultRouteState': 'reachable',
#                                   'routes': {'0.0.0.0/0': {'directlyConnected': False,
#                                                            'hardwareProgrammed': True,
#                                                            'kernelProgrammed': True,
#                                                            'metric': 0,
#                                                            'preference': 1,
#                                                            'routeAction': 'forward',
#                                                            'routeType': 'static',
#                                                            'vias': [{'interface': 'Vlan1',
#                                                                      'nexthopAddr': '10.220.88.1'}]},
#                                              '10.220.88.0/24': {'directlyConnected': True,
#                                                                 'hardwareProgrammed': True,
#                                                                 'kernelProgrammed': True,
#                                                                 'routeAction': 'forward',
#                                                                 'routeType': 'connected',
#                                                                 'vias': [{'interface': 'Vlan1'}]}},
#                                   'routingDisabled': False}}}}]
# 
