from napalm import get_network_driver
import json

driver = get_network_driver("ios")

optional_args = {'secret': 'cisco'}
ios = driver("10.1.1.20", "u1", "cisco", optional_args=optional_args)

ios.open()

# start your code

ios.load_replace_candidate(filename="current_config.txt")

diff = ios.compare_config()

if len(diff):
    print(diff)
    print("committing changes...")
    ios.commit_config()
    print("Configuration updated")
else:
    print("No changes required")
    ios.discard_config()

# end your code

ios.close()