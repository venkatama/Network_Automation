import paramiko
import time
import threading

def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd,
                       look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timout)

def send_from_list(shell, cmdlist, timeout=1):
    for command in cmdlist:
        shell.send(command + '\n')
    time.sleep(timeout)

def send_from_file(shell, txtfile, timeout=1):
    cmdlist = list()
    with open(txtfile) as readfile:
        cmdlist = readfile.read().splitlines()
    send_from_list(shell, cmdlist, timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

if __name__ == '__main__':
    router1 = {'server_ip': '192.168.122.10', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco',
               'config': 'ospf.txt'}

    router2 = {'server_ip': '192.168.122.20', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco',
               'config': 'eigrp.txt'}

    router3 = {'server_ip': '192.168.122.30', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco',
               'config': 'router3.conf'}
    routers = [router1, router2, router3]
    threads= list()
    for router in routers:
        client = connect(router["server_ip"], router["server_port"], router["user"], router["passwd"])
        shell = get_shell(client)
        send_from_file(shell, router["config"], timeout=2)
        output = show(shell)
        print(output)
