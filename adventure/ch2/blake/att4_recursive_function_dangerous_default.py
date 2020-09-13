"""
Use a `deque` and a `while` loop in a recursive function to solve "Chapter 2 - Fibonacci
frailty".
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
    Tells the tale of the mage's journey to the bench.
    """

    # Here we go
    stamina_left = fibonacci_frailty(
        stamina=STAMINA,
        steps_till_bench=STEPS_TILL_BENCH,
    )
    print(f"After all that, the mage had {stamina_left} stamina left.\n")

    # Once more, with feeling
    stamina_left = fibonacci_frailty(
        stamina=STAMINA,
        steps_till_bench=STEPS_TILL_BENCH,
    )
    print(f"After all that, the mage had {stamina_left} stamina left.\n")


# * ------------------------------------------------------------------------------ # *
# * FUNCTION * #


FIBONACCI_SEQUENCE = deque([0, 1], maxlen=2)
INITIAL_STEPS = 2

#! What is a "dangerous default"? Let's find out! Linters are your friend.
def fibonacci_frailty(
    stamina,
    steps_till_bench,
    steps_taken=INITIAL_STEPS,
    fibonacci_sequence=FIBONACCI_SEQUENCE,
):
    """
    Reduce the mage's stamina for each step taken, according to the Fibonacci sequence.
    """

    # Take the first two steps in the first call to this function
    if steps_taken == INITIAL_STEPS:
        stamina -= 1
        print(
            "The mage has lost one stamina in his initial steps,"
            f" and has {stamina} stamina left."
        )

    # The mage takes another step with each recursive call to the function
    if steps_taken < steps_till_bench and stamina > 0:
        steps_taken += 1

        stamina_loss_this_step = sum(fibonacci_sequence)
        stamina -= stamina_loss_this_step
        fibonacci_sequence.append(stamina_loss_this_step)

        print(
            f"He has taken {steps_taken} steps,"
            f" lost {stamina_loss_this_step} stamina this step,"
            f" and has {stamina} stamina left."
        )

        #! Remember when you called `sequence.append(stamina_loss_this_step)` directly
        #! and it didn't work because you forgot that it returns `None`.
        stamina = fibonacci_frailty(
            stamina, steps_till_bench, steps_taken, fibonacci_sequence
        )

    if steps_taken == INITIAL_STEPS + 1:
        if stamina > 0:
            print("The mage has made it to the bench.\n")
        else:
            print("He is out of stamina. He spirals inward and collapses.\n")

    return stamina


# * ------------------------------------------------------------------------------ # *
# * RUN MAIN * #

if __name__ == "__main__":
    main()
