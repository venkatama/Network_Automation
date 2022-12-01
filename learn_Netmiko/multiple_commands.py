from netmiko import Netmiko
from netmiko import ConnectHandler
#connection = Netmiko(host="192.168.122.10", port="22", username="u1", password="cisco", device_type="cisco_ios")

cisco_device = {
    "device_type": "cisco_ios",
    "host": "192.168.122.10",
    "username": "u1",
    "password": "cisco",
    "port": "22",
    "secret": "cisco",
    "verbose": True
}

connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()
print(prompt)
if ">" in prompt:
    print("Entering into enable mode...")
    connection.enable()

with open("ospf.txt") as cmdlist:
    commands = cmdlist.read().splitlines()

output = connection.send_config_from_file("ospf.txt")
print(output)
connection.disconnect()
