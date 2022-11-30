import paramiko
import time
import getpass
import csv

# Reading data from csv file

password = getpass.getpass("Enter Password: ")
with open("routers.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    routers = list()
    for row in csvreader:
        router = dict()
        router["hostname"] = row[0]
        router["port"]= row[1]
        router["username"]= row[2]
        router["password"]= password
        routers.append(router)

print(routers)

for router in routers:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(**router, allow_agent=False, look_for_keys=False)
    print(f'connecting to {router["hostname"]}')
    shell = ssh_client.invoke_shell()
    shell.send("enable\n")
    shell.send("cisco\n")
    shell.send("conf t\n")
    shell.send("sh ip ospf neighbor")
    shell.send("no router ospf 1\n")
    shell.send("router ospf 1\n")
    shell.send("net 0.0.0.0 0.0.0.0 area 0\n")
    shell.send("end\n")
    shell.send("terminal length 0\n")
    shell.send("sh ip protocols\n")
    shell.send("sh ip ospf neighbor\n")
    time.sleep(2)
    output = shell.recv(10000).decode('utf-8')
    print(output)

    if ssh_client.get_transport().is_active() == True:
        print("closing connection")
        ssh_client.close()