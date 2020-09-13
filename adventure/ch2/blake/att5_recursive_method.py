"""
Use a `deque` and a `while` loop in a recursive class method to solve "Chapter 2 -
Fibonacci frailty".
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

    stamina_left = walk_to_bench(STAMINA, STEPS_TILL_BENCH)
    print(f"After all that, the mage had {stamina_left} stamina left.")


# * ------------------------------------------------------------------------------ # *
# * FUNCTIONS AND CLASSES * #


def walk_to_bench(stamina, steps_till_bench):
    """
    Walk to the bench under the influence of Fibonacci frailty.
    """

    condition = FibonacciFrailty(stamina)
    condition.first_steps(steps_till_bench)
    stamina_left = condition.next_steps()

    if stamina_left > 0:
        print("The mage has made it to the bench.")
    else:
        print("He is out of stamina. He spirals inward and collapses.")

    return stamina_left


class FibonacciFrailty:
    """
    Reduce the mage's stamina for each step taken, according to the Fibonacci sequence.
    """

    def __init__(self, stamina):

        self.stamina = stamina

        self.steps_taken = None
        self.steps_till_bench = None
        self.fibonacci_sequence = None

    def first_steps(self, steps_till_bench):
        """
        Apply the first steps of Fibonacci Frailty.
        """

        self.steps_taken = 2
        self.steps_till_bench = steps_till_bench
        self.stamina -= 1
        self.fibonacci_sequence = deque([0, 1], maxlen=2)
        print(
            "The mage has lost one stamina in his initial steps,"
            f" and has {self.stamina} stamina left."
        )

    def next_steps(self):
        """
        Apply the next steps of Fibonacci Frailty.
        """

        # The mage takes another step with each recursive call to the function
        if self.steps_taken < self.steps_till_bench and self.stamina > 0:
            self.steps_taken += 1

            stamina_loss_this_step = sum(self.fibonacci_sequence)
            self.stamina -= stamina_loss_this_step
            self.fibonacci_sequence.append(stamina_loss_this_step)

            print(
                f"He has taken {self.steps_taken} steps,"
                f" lost {stamina_loss_this_step} stamina this step,"
                f" and has {self.stamina} stamina left."
            )

            #! Going forward, do we really want this to be recursive? Maybe we want to
            #! define a `step` method  that applies status effects on each step?

            self.stamina = self.next_steps()

        return self.stamina


# * ------------------------------------------------------------------------------ # *
# * RUN MAIN * #

if __name__ == "__main__":
    main()
