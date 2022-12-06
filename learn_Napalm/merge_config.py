from napalm import get_network_driver
import json

driver = get_network_driver("ios")

optional_args = {'secret': 'cisco'}
ios = driver("10.1.1.20", "u1", "cisco", optional_args=optional_args)

ios.open()

# start your code

ios.load_merge_candidate(filename="acl.txt")

diff = ios.compare_config()

if len(diff):
    print(diff)
    answer = input("Commit changes?<yes|no>: ")
    if answer == "yes":
        print("committing changes...")
        ios.commit_config()
        print("Configuration updated")
    else:
        print("No changes required")
        ios.discard_config()
else:
    print("No changes required")

# end your code

ios.close()

# end your code

ios.close()