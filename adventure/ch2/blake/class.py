"""
The mage's toenail is throbbing from where the bramble patch really got him good. As he
neas the end of his thorny journey, the mage notices the beautifully coiled vines beside
the path. Those vines coiled in the Golden Ratio could only mean one thing, this was
Fibonacci Weed! The mage could already feel it setting in, that terrible condition known
as Fibonacci frailty!

Excerpt from a book, from the mage's diverse library:

    Fibonacci Frailty: Not so bad, at first. On the first step, the victim feels
    no loss of vigor. But the second step saps one (1) stamina. Every step thereafter
    saps as much stamina as the previous two steps combined. On the third step,
    one (1) stamina is lost. The fourth steals two (2). Then 3, 5, and 8.

? The mage sees a bench in the market square. It is eleven steps away. Will he make it?
? For each step he takes, how much stamina does he lose and how much stamina does he
? have left? Does he reach the bench?
"""

from collections import deque

# * ------------------------------------------------------------------------------ # *
# * SETUP * #

STAMINA = 150
STEPS_TILL_BENCH = 11

FIBONACCI_SEQUENCE = deque([0, 1], maxlen=2)
INITIAL_STEPS = 2

# * ------------------------------------------------------------------------------ # *
# * MAIN * #


def main():
    """
    Tells the tale of the mage's journey to the bench.
    """

    FibonacciContainer(
        stamina=STAMINA,
        steps_taken=INITIAL_STEPS,
        num_steps=STEPS_TILL_BENCH,
        sequence=FIBONACCI_SEQUENCE,
    )


# * ------------------------------------------------------------------------------ # *
# * FUNCTION * #


class FibonacciContainer:
    """
    Reduces stamina with each step taken, following a Fibonacci sequence. If stamina is
    reduced to zero, the victim collapses. Returns the stamina remaining if the
    destination is reached.
    """

    def __init__(self, stamina, steps_taken, num_steps, sequence):
        self.msg = ""
        self.stamina_left = self.fibonacci_frailty(
            stamina, steps_taken, num_steps, sequence
        )
        if self.stamina_left > 0:
            print("The mage has made it to the bench.")
        else:
            print("He is out of stamina. He spirals inward and collapses.")

    def fibonacci_frailty(self, stamina, steps_taken, num_steps, sequence):
        """
        Reduces stamina with each step taken, following a Fibonacci sequence. If stamina
        is reduced to zero, the victim collapses. Returns the stamina remaining if the
        destination is reached.
        """

        if steps_taken == 2:
            stamina -= 1
            self.msg = "The mage has lost one stamina in his initial steps."
            if stamina < 1:
                self.msg += " He is out of stamina. He spirals inward and collapses."
            else:
                self.msg += f" He has {stamina} stamina left."
            print(self.msg)

        if stamina > 0 and steps_taken < num_steps:

            steps_taken += 1
            stamina_loss_this_step = sum(sequence)
            stamina -= stamina_loss_this_step

            self.msg = f"The mage has taken {steps_taken} steps."
            self.msg += f" He lost {stamina_loss_this_step} stamina this step."
            self.msg += f" He has {stamina} stamina left."
            print(self.msg)

            sequence.append(stamina_loss_this_step)

            stamina = self.fibonacci_frailty(
                stamina=stamina,
                num_steps=num_steps,
                steps_taken=steps_taken,
                sequence=sequence,
            )

        return stamina


# * ------------------------------------------------------------------------------ # *
# * RUN MAIN * #

if __name__ == "__main__":
    main()
