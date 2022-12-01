import paramiko
import time
import threading

def execute_command(device, commands):

    # creating an ssh client object
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    print(f'Connecting to {device["hostname"]}')
    ssh_client.connect(**device)


    shell = ssh_client.invoke_shell()
    shell.send('term length 0\n')
    for command in commands:
        print(f'Sending command "{command}" to "{device["hostname"]}"')
        shell.send(f'{command}\n')
    time.sleep(1)

    output = shell.recv(100000).decode()
    print(output)


    if ssh_client.get_transport().is_active():
        print('Closing connection')
        ssh_client.close()


if __name__ == '__main__':
    router1 = {'hostname': '192.168.122.10', 'port': '22', 'username': 'u1', 'password': 'cisco',
                  'look_for_keys': False, 'allow_agent': False}
    router2 = {'hostname': '192.168.122.20', 'port': '22', 'username': 'u1', 'password': 'cisco',
                  'look_for_keys': False, 'allow_agent': False}
    router3 = {'hostname': '192.168.122.30', 'port': '22', 'username': 'u1', 'password': 'cisco',
                  'look_for_keys': False, 'allow_agent': False}

    routers = [router1, router2, router3]

    with open("commands.txt") as f:
        commands = f.read().splitlines()

    threads = list()
    for device in routers:
        th = threading.Thread(target=execute_command, args=(device, commands))
        threads.append(th)

    for th in threads:
        th.start()


    for th in threads:
        th.join()