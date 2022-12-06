from netmiko import Netmiko
from netmiko import ConnectHandler
# connection = Netmiko(host="192.168.122.10", port="22", username="u1", password="cisco", device_type="cisco_ios")

devices = ["10.1.1.20", "10.1.1.30", "10.1.1.40"]

for device in devices:
    cisco_device = {
        "device_type": "cisco_ios",
        "host": device,
        "username": "u1",
        "password": "cisco",
        "port": "22",
        "secret": "pass123",
        "verbose": True
    }

    connection = ConnectHandler(**cisco_device)
    prompt = connection.find_prompt()
    if ">" in prompt:
        print("Entering into enable mode...")
        connection.enable()

    output = connection.send_command("show run")
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]
    filename = f'{hostname}-backup.txt'
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'{hostname} backup has been created with the name {filename}')
    print("Closing the connection for {}".format(hostname))
    connection.disconnect()

