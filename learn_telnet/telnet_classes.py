import time
import threading

class Tdevice:
    def __init__(self, host, username, password, tn=None):
        self.host = host
        self.username = username
        self.password = password
        self.tn = tn

    def connect(self):
        import telnetlib
        print(f"Connecting to {self.host}")
        self.tn = telnetlib.Telnet(self.host)

    def authentication(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')

        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')

    def send(self, command, timeout=0.5):
        print(f"sending the command : {command}")
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)

    def send_from_list(self, commands, timeout=0.5):
        for command in commands:
#            print(f"sending command : {command}")
            self.tn.write(command.encode() + b"\n")

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output

commands = ['conf t', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit',
            'router ospf 1', 'net 0.0.0.0 0.0.0.0 area 0', 'end', 'term len 0', 'show ip protocols', 'exit']

with open("routers.txt") as r:
    routers = r.read().splitlines()


def execute_command(rou):
    route = rou.split(":")
    router = Tdevice(host=route[0], username=route[1], password=route[2])
    router.connect()
    router.authentication()
    router.send_from_list(commands)
    print(router.show())
    print(50 * "#")


threads = list()

for route in routers:
    tn = threading.Thread(target=execute_command, args=(route,))
    threads.append(tn)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()











