"""
This is one possible solution to Chapter 2: Fibonacci frailty
"""

from collections import deque

# The mage's initial condition
STAMINA = 150
STEPS_TILL_BENCH = 11

# Take the first two steps outside of the loop
# ? A `deque` has a fixed length. When we `append` a new element, an old element gets
# ? deleted.
FIBONACCI_SEQUENCE = deque([0, 1], maxlen=2)
STEPS_TAKEN = 2
STAMINA -= 1
print(
    "The mage has lost one stamina in his initial steps,"
    f" and has {STAMINA} stamina left.\n"
)
# The mage takes another step with each iteration of the loop

while STEPS_TAKEN < STEPS_TILL_BENCH and STAMINA > 0:
    STEPS_TAKEN = STEPS_TAKEN + 1
    damage_this_step = sum(FIBONACCI_SEQUENCE)
    # Decrement stamina this step.
    STAMINA -= damage_this_step

    # Update FIBONACCI_SEQUENCE with the latest step
    FIBONACCI_SEQUENCE.append(damage_this_step)
