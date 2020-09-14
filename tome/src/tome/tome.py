"""
One possible solution to the Story of a Mage.
"""

from collections import deque


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
        #! Generalized "bench" out of this statement
        print("The mage has made it to his destination.\n")
    else:
        print("The mage is out of stamina. He spirals inward and collapses.\n")

    return stamina
