"""
One possible solution to "Chapter 3 - The Traveling Mage Problem".
"""

import os
import yaml
from storybook import Mage, FibonacciFrailty

STAMINA = 150
mage = Mage()
mage.contract(FibonacciFrailty)

with open(os.environ["STORYBOOK_STORE_DIR"]) as file:
    directory = yaml.safe_load(file)

potion_directory = {}

for store, distance in directory.items():
    if "potion" in store.lower():
        potion_directory[store] = distance

sorted_by_distance = sorted(potion_directory, key=potion_directory.__getitem__)
closest_potion_shop = sorted_by_distance[0]
steps_till_shop = potion_directory[closest_potion_shop]

for _ in range(steps_till_shop):
    mage.step()
    print(mage.condition)