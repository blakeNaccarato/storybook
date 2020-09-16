"""
This is one possible solution to Chapter 1: A thorny situation.
"""

HEALTH = 20
DAMAGE = [2, 1, 4, 1]

for damage_this_step in DAMAGE:
    HEALTH -= damage_this_step
    print(HEALTH)
