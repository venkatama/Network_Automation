from napalm import get_network_driver
import json
import getpass

driver = get_network_driver("ios")

optional_args = {'secret': 'cisco'}
ios = driver("10.1.1.20", "u1", "cisco", optional_args=optional_args)

ios.open()

# start your code

ios.load_merge_candidate(filename="acl.txt")

diff = ios.compare_config()
ios.rollback()

# end your code

ios.close()
