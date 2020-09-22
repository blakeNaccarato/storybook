"""
Use a `deque` and a `while` loop in a function to solve "Chapter 2 - Fibonacci frailty".
"""

from collections import deque


# * ------------------------------------------------------------------------------ # *
# * SETUP * #

STAMINA = 150
STEPS_TILL_BENCH = 11

# * ------------------------------------------------------------------------------ # *
# * MAIN * #


def main():
    """
    The main function that will run when this file is invoked directly.
    """

    stamina_left = fibonacci_frailty(STAMINA, STEPS_TILL_BENCH)
    print(f"After all that, the mage had {stamina_left} stamina left.\n")


# * ------------------------------------------------------------------------------ # *
# * FUNCTIONS * #


def fibonacci_frailty(stamina, steps_till_bench):
    """
    Reduce the mage's stamina for each step taken, according to the Fibonacci sequence.
    """

    # Take the first two steps outside of the loop
    steps_taken = 2
    fibonacci_sequence = deque([0, 1], maxlen=2)
    stamina -= 1
    print(
        "The mage has lost one stamina in his initial steps,"
        f" and has {stamina} stamina left."
    )

    # The mage takes another step with each iteration of the loop
    while steps_taken < steps_till_bench and stamina > 0:
        steps_taken += 1

        stamina_loss_this_step = sum(fibonacci_sequence)
        stamina -= stamina_loss_this_step
        fibonacci_sequence.append(stamina_loss_this_step)

        print(
            f"He has taken {steps_taken} steps,"
            f" lost {stamina_loss_this_step} stamina this step,"
            f" and has {stamina} stamina left."
        )

    if stamina > 0:
        print("The mage has made it to the bench.\n")
    else:
        print("The mage is out of stamina. He spirals inward and collapses.\n")

    return stamina


# * ------------------------------------------------------------------------------ # *
# * RUN MAIN * #

if __name__ == "__main__":
    main()
