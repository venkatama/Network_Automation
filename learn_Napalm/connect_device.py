from napalm import get_network_driver
import json

driver = get_network_driver("ios")

optional_args = {'secret' : 'cisco'}
ios = driver("10.1.1.20", "u1", "cisco", optional_args=optional_args)

ios.open()

#start your code

output = ios.get_facts()
dump = json.dumps(output, sort_keys=True, indent=4)

output = ios.get_config()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

#with open("facts.txt", "w") as arp:
#    arp.write(dump)

#end your code

ios.close()