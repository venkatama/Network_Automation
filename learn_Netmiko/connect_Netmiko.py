from netmiko import Netmiko
from netmiko import ConnectHandler
#connection = Netmiko(host="192.168.122.10", port="22", username="u1", password="cisco", device_type="cisco_ios")

cisco_device={
    "device_type": "cisco_ios",
    "host": "192.168.122.10",
    "username": "u1",
    "password": "cisco",
    "port": "22",
    "secret": "cisco",
    "verbose": True
}

connection = ConnectHandler(**cisco_device)
output = connection.send_command("sh ip int brief")
print(output)
connection.disconnect()
