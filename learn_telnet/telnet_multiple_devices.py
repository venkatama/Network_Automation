import telnetlib
import time
import getpass

with open("routers.txt") as r:
    routers = r.read().splitlines()

with open("ospf.txt") as ospf:
    commands = ospf.read().splitlines()

password = getpass.getpass("Enter password to connect to device..: ")
for router in routers:
    router = router.split(":")
    print(f"connecting to {router[0]}....")
    tn = telnetlib.Telnet(host=router[0])

    tn.read_until(b'Username: ')
    tn.write(router[1].encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'terminal length 0\n')
    command = "show users"
    tn.write(command.encode() + b'\n')
    tn.write(b'exit\n')
    time.sleep(1)
    output = tn.read_all()
    print(output.decode())
    print(30 * "#")

