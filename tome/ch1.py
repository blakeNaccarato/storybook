"""
Blake's working script for "Chapter 1 - A thorny situation".
"""

HEALTH = 20
DAMAGE_EACH_STEP = [2, 1, 4, 1]

for damage_this_step in DAMAGE_EACH_STEP:
    HEALTH -= damage_this_step
    print(
        f"The mage took {damage_this_step} damage this step."
        f" He has {HEALTH} health left."
    )
