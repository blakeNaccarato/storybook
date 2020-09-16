"""
Use a `deque` and a `while` loop to solve "Chapter 2 - Fibonacci frailty".
"""

from collections import deque

# The mage's initial condition
STAMINA = 150
STEPS_TILL_BENCH = 11

# Take the first two steps outside of the loop
#? A `deque` has a fixed length. When we `append` a new element, an old element gets
#? deleted.
FIBONACCI_SEQUENCE = deque([0, 1], maxlen=2)
STEPS_TAKEN = 2
STAMINA -= 1
print(
    "The mage has lost one stamina in his initial steps,"
    f" and has {STAMINA} stamina left.\n"
)
# The mage takes another step with each iteration of the loop
while STEPS_TAKEN < STEPS_TILL_BENCH and STAMINA > 0:
    STEPS_TAKEN += 1  #? Try to increment either at the very beginning or very end

    #? Summing the two-element `deque` gives us the stamina loss for this step.
    stamina_loss_this_step = sum(FIBONACCI_SEQUENCE)
    STAMINA -= stamina_loss_this_step  #? Make sure all variables in `while` get used
    FIBONACCI_SEQUENCE.append(stamina_loss_this_step)

    #? Beware of printing before the end of a loop iteration. The values of variables
    #? might not reflect the actual flow of the code.
    print(
        f"He has taken {STEPS_TAKEN} steps,"
        f" lost {stamina_loss_this_step} stamina this step,"
        f" and has {STAMINA} stamina left."
    )

#? The loop has ended because the mage either made it to the bench or ran out of stamina
if STAMINA > 0:
    print("The mage has made it to the bench.\n")
else:
    print("The mage is out of stamina. He spirals inward and collapses.\n")
