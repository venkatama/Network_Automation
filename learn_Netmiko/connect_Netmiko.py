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
    connection.enable()
output = connection.send_command("sh run | include user")
print(output)
if not connection.check_config_mode():
    connection.config_mode()

print(connection.check_config_mode())

connection.send_command("username u4 secret cisco")
connection.exit_config_mode()
print(connection.check_config_mode())
connection.disconnect()
