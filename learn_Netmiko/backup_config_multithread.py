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
    prompt = connection.find_prompt()
    if ">" in prompt:
        print("Entering into enable mode...")
        connection.enable()

    output = connection.send_command("show run")
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]
    now = datetime.now()
    filename = f'{hostname}_{now.year}-{now.month}-{now.day}_backup.txt'
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'{hostname} backup has been created with the name {filename}')
    print("Closing the connection for {}".format(hostname))
    connection.disconnect()
    print(20  * "#")

devices = ["192.168.122.10", "192.168.122.20", "192.168.122.30"]

threads = list()


for device in devices:
    cisco_device = {
        "device_type": "cisco_ios",
        "host": device,
        "username": "u1",
        "password": "cisco",
        "port": "22",
        "secret": "cisco",
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

