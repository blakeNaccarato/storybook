"""
Blake's dictionary-based solution to "Chapter 3 - The Traveling Mage Problem". Uses
environment variables.
"""

import yaml
from tome import fibonacci_frailty

STAMINA = 150

#TODO: Use an environment variable instead of a hardcoded path
STORE_DIRECTORY_PATH = r"adventure\ch3\Ye_olde_store_directory.yaml"

with open(STORE_DIRECTORY_PATH) as file:
    directory = yaml.safe_load(file)

potion_directory = {}

for store, distance in directory.items():
    if "potion" in store.lower():
        potion_directory[store] = distance

sorted_by_distance = sorted(potion_directory, key=potion_directory.__getitem__)
closest_potion_shop = sorted_by_distance[0]
steps_till_shop = potion_directory[closest_potion_shop]
stamina_left = fibonacci_frailty(STAMINA, steps_till_shop)
