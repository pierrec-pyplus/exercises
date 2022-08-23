from netmiko import ConnectHandler

def ssh_command(my_dev, my_sho_command):
    net_connect = ConnectHandler(**my_dev)
    output = net_connect.send_command_expect(my_sho_command)
    print("-" * 20)
    print(my_dev['host'])
    print(output)
    print("-" * 20)

def ssh_command2(my_dev, my_sho_command):
    net_connect = ConnectHandler(**my_dev)
    output = net_connect.send_command_expect(my_sho_command)
    return output
