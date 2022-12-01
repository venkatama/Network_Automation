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

with open("commands.txt") as f:
    commands = f.read().splitlines()

for router in routers:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(**router, allow_agent=False, look_for_keys=False)
    print(f'connecting to {router["hostname"]}')
    shell = ssh_client.invoke_shell()
#    commands = list()
#    commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user']
    for command in commands:
        shell.send(command + "\n")
    time.sleep(2)
    output = shell.recv(10000).decode('utf-8')
    print(output)

    if ssh_client.get_transport().is_active() == True:
        print("closing connection")
        ssh_client.close()