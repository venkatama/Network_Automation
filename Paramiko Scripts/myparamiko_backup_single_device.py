import myparamiko # myparamiko.py should be in the same directory with this script (or in sys.path)

router = {'server_ip':'192.168.122.30', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
client = myparamiko.connect(**router)
shell = myparamiko.get_shell(client)

myparamiko.send_command(shell, 'terminal length 0')
myparamiko.send_command(shell, 'enable')
myparamiko.send_command(shell, 'cisco')  # this is the enable command
myparamiko.send_command(shell, 'show run')

output = myparamiko.show(shell)
# processing the output
# print(output)
output_list = output.splitlines()
output_list = output_list[11:-1]
# print(output_list)
output = '\n'.join(output_list)
# print(output)

# creating the backup filename
from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

file_name = f'{router["server_ip"]}_{year}-{month}-{day}.txt'
print(file_name)

# writing the backup to the file
with open(file_name, 'w') as f:
    f.write(output)

myparamiko.close(client)
