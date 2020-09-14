"""
Use a `deque` and a `while` loop in a function to solve "Chapter 2 - Fibonacci frailty".
Uses global variables, and the function takes no arguments.
"""

from collections import deque


# * ------------------------------------------------------------------------------ # *
# * SETUP * #

# The mage's initial condition
STAMINA = 150
STEPS_TILL_BENCH = 11

# * ------------------------------------------------------------------------------ # *
# * MAIN * #


def main():
    """
    The main function that will run when this file is invoked directly.
    """

    fibonacci_frailty()


# * ------------------------------------------------------------------------------ # *
# * FUNCTIONS SETUP * #

# Setup for `fibonacci_frailty()`
FIBONACCI_SEQUENCE = deque([0, 1], maxlen=2)
STEPS_TAKEN = 2

# * ------------------------------------------------------------------------------ # *
# * FUNCTIONS * #


def fibonacci_frailty():
    """
    Reduce the mage's stamina each step according to the Fibonacci sequence.
    """

    #! We should try to avoid globals whenever we can!
    global STAMINA, STEPS_TAKEN

    # Take the first two steps outside of the loop
    STAMINA -= 1
    print(
        "The mage has lost one stamina in his initial steps,"
        f" and has {STAMINA} stamina left.\n"
    )

    # The mage takes another step with each iteration of the loop
    while STEPS_TAKEN < STEPS_TILL_BENCH and STAMINA > 0:
        STEPS_TAKEN += 1

        stamina_loss_this_step = sum(FIBONACCI_SEQUENCE)
        STAMINA -= stamina_loss_this_step
        FIBONACCI_SEQUENCE.append(stamina_loss_this_step)

        print(
            f"He has taken {STEPS_TAKEN} steps,"
            f" lost {stamina_loss_this_step} stamina this step,"
            f" and has {STAMINA} stamina left."
        )

    if STAMINA > 0:
        print("The mage has made it to the bench.\n")
    else:
        print("The mage is out of stamina. He spirals inward and collapses.")


# * ------------------------------------------------------------------------------ # *
# * RUN MAIN * #

if __name__ == "__main__":
    main()
