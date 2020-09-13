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

stamina = 150
STEPS_TILL_BENCH = 11

FIBONACCI_SEQUENCE = deque([0, 1], maxlen=2)


def fibonacci_frailty(stamina):

    steps_taken = 2
    stamina -= 1
    MSG = "The mage has lost one stamina in his initial steps."

    if stamina < 1:
        MSG += " He is out of stamina. He spirals inward and collapses."
        MSG += f" He has {stamina} stamina left."
        print(MSG)

    while steps_taken < STEPS_TILL_BENCH and stamina > 0:

        steps_taken += 1
        stamina_loss_this_step = sum(FIBONACCI_SEQUENCE)
        stamina -= stamina_loss_this_step

        MSG = f"The mage has taken {steps_taken} steps."
        MSG += f" He lost {stamina_loss_this_step} stamina this step."
        MSG += f" He has {stamina} stamina left."
        print(MSG)

        FIBONACCI_SEQUENCE.append(stamina_loss_this_step)

    if stamina > 0:
        print("The mage has made it to the bench.")
    else:
        print("He is out of stamina. He spirals inward and collapses.")
