from napalm import get_network_driver
import json

driver = get_network_driver("ios")

optional_args = {'secret': 'cisco'}
ios = driver("10.1.1.20", "u1", "cisco", optional_args=optional_args)

ios.open()

# start your code

output = ios.ping(destination="10.1.1.30", count=2, source="10.1.1.20")
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

#with open("facts.txt", "w") as arp:
#    arp.write(dump)

# end your code

ios.close()