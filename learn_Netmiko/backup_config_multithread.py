from netmiko import Netmiko
from netmiko import ConnectHandler
import threading
from datetime import datetime
import time
import logging
logging.basicConfig(filename="netmikologs.txt", level=logging.DEBUG)
logger = logging.getLogger("netmiko")
# connection = Netmiko(host="192.168.122.10", port="22", username="u1", password="cisco", device_type="cisco_ios")
start = time.time()
def backup_router(device):
    connection = ConnectHandler(**device)
    print("Entering into enable mode...")
    connection.enable()
    connection.exit_config_mode()
    connection.exit_config_mode()
    commands = ["show arp", "show ip int brief"]
    output = list()
    for command in commands:
        output.append(connection.send_command(command))
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]
    now = datetime.now()
    filename = f'{hostname}_{now.year}-{now.month}-{now.day}_backup.txt'
    with open(filename, 'a') as backup:
        for finalout in output:
            backup.write(finalout)
        print(f'{hostname} backup has been created with the name {filename}')
    print("Closing the connection for {}".format(hostname))
    connection.disconnect()
    print(20  * "#")

with open("routers.txt") as routers:
    devices = routers.read().splitlines()

threads = list()


for device in devices:
    cisco_device = {
        "device_type": "cisco_ios",
        "host": device.split(":")[0],
        "username": device.split(":")[2],
        "password": device.split(":")[3],
        "port": device.split(":")[1],
        "secret": device.split(":")[4],
        "verbose": True
    }
    th = threading.Thread(target=backup_router, args=(cisco_device,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

end = time.time()
print(f'Total time taken for execution{end-start}')

