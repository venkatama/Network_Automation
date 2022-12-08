import telnetlib
import time

router1 = {'host': '10.1.1.20', 'user': 'u1', 'password': 'cisco'}
router2 = {'host': '10.1.1.30', 'user': 'u1', 'password': 'cisco'}
router3 = {'host': '10.1.1.40', 'user': 'u1', 'password': 'cisco'}

routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["host"]}')

    tn = telnetlib.Telnet(host=router['host'])

    tn.read_until(b'Username: ')
    tn.write(router['user'].encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(router['password'].encode() + b'\n')

    tn.write(b'terminal length 0\n')

    tn.write(b'conf t\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 FastEthernet0/0 10.1.1.2\n')
    tn.write(b'end\n')
    tn.write(b'show ip route\n')
    tn.write(b'exit\n')
    time.sleep(1)

    output = tn.read_all()
    output = output.decode()
    print(output)
    print('#' * 50)