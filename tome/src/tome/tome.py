"""
One possible solution to the Story of a Mage.
"""

from collections import deque


class FibonacciFrailty:
    """
    Reduce the mage's stamina for each step taken, according to the Fibonacci sequence.
    """

    def __init__(self, stamina):

        self.stamina = stamina
        self.stamina_loss_this_step = 0
        self.steps_since_rest = 0
        self.fibonacci_sequence = deque(maxlen=2)

    def __repr__(self):
        """
        Print the result of the latest step.
        """

        return (
            f"Steps taken: {self.steps_since_rest:3},"
            f" Stamina lost this step: {self.stamina_loss_this_step:3},"
            f" Stamina left: {self.stamina:3}."
        )

    def step(self):
        """
        Take one step under the influence of Fibonacci Frailty.
        """

        if self.steps_since_rest == 0:
            self.accumulate(0)
        elif self.steps_since_rest == 1:
            self.accumulate(1)
        else:
            self.accumulate(sum(self.fibonacci_sequence))

        return self.stamina

    def accumulate(self, stamina_loss_this_step):
        """
        Accumulate stamina loss, keeping a two-step history of stamina lost.
        """

        self.steps_since_rest += 1
        self.stamina_loss_this_step = stamina_loss_this_step
        self.stamina -= self.stamina_loss_this_step
        self.fibonacci_sequence.append(self.stamina_loss_this_step)


# * ------------------------------------------------------------------------------ # *
# * EARLIER IMPLEMENTATIONS * #


def fibonacci_frailty(stamina, steps_till_destination):
    """
    Reduce the mage's stamina for each step taken, according to the Fibonacci sequence.
    """

    # Take the first two steps outside of the loop
    steps_since_rest = 2
    fibonacci_sequence = deque([0, 1], maxlen=2)
    stamina -= 1
    print(
        "The mage has lost one stamina in his initial steps,"
        f" and has {stamina} stamina left."
    )

    # The mage takes another step with each iteration of the loop
    while steps_since_rest < steps_till_destination and stamina > 0:
        steps_since_rest += 1

        stamina_loss_this_step = sum(fibonacci_sequence)
        stamina -= stamina_loss_this_step
        fibonacci_sequence.append(stamina_loss_this_step)

        print(
            f"He has taken {steps_since_rest} steps,"
            f" lost {stamina_loss_this_step} stamina this step,"
            f" and has {stamina} stamina left."
        )

    if stamina > 0:
        #! Generalized "bench" out of this statement
        print("The mage has made it to his destination.\n")
    else:
        print("The mage is out of stamina. He spirals inward and collapses.\n")

    return stamina
