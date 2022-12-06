from netmiko import ConnectHandler
from netmiko import file_transfer

device = {
        "device_type": "linux",
        "host": "10.1.1.10",
        "username": "mani",
        "password": "pass123",
        "port": "22",
        "secret": "pass123",
        "verbose": True
    }
connection = ConnectHandler(**device)

transfer_output = file_transfer(connection, source_file="ospf.txt", dest_file="ospf1.txt", file_system="disk0:",
                                direction="put", overwrite_file=True)

print(transfer_output)
connection.disconnect()