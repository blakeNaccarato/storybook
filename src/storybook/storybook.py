"""
A collaboration in Python.
"""

from collections import deque


# * ------------------------------------------------------------------------------ # *
# * CHAPTERS * #

CH1_INITIAL_HEALTH = 100
CH1_DAMAGE_EACH_STEP = [2, 1, 4, 1]


def ch1(mage=None):
    """
    Chapter 1 of Story of a Mage.
    """

    if not mage:
        mage = Mage()

    for damage_this_step in CH1_DAMAGE_EACH_STEP:
        mage.health -= damage_this_step

    return mage


# * ------------------------------------------------------------------------------ # *
# * CODE * #


class Mage:
    """
    A mage on a journey.
    """

    INITIAL_HEALTH = 100
    INITIAL_STAMINA = 150

    def __init__(self):

        self.health = self.INITIAL_HEALTH
        self.stamina = self.INITIAL_STAMINA
        self.condition = None
        self.purse = {"gold": 2, "silver": 40}  # coin type: quantity
        self.pouch = {"pemmican": 1}  # item: quantity
        self.spells = {"Restore Stamina": 50, "Ranged Reach": 20}  # spell: cooldown

    def contract(self, condition):
        """
        Become afflicted with a condition.
        """

        self.condition = condition(self)

    def step(self):
        """
        Take a step.
        """

        if self.condition:
            self.condition.step()


class FibonacciFrailty:
    """
    Reduce the mage's stamina for each step taken, according to the Fibonacci sequence.
    """

    def __init__(self, target):

        self.target = target
        self.stamina = target.stamina
        self.stamina_lost_this_step = None
        self.steps_since_rest = None
        self.fibonacci_sequence = None
        self.reset()

    def __repr__(self):
        """
        Print the result of the latest step.
        """

        return (
            f"{type(self).__name__}:"
            f" Steps taken: {self.steps_since_rest},"
            f" Stamina lost this step: {self.stamina_lost_this_step},"
            f" Stamina left: {self.stamina}."
        )

    def steps(self, num_steps):
        """
        Take multiple steps under the influence of Fibonacci Frailty.
        """

        for _ in range(num_steps):
            self.step()

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

    def accumulate(self, stamina_lost_this_step):
        """
        Accumulate stamina loss, keeping a two-step history of stamina lost.
        """

        self.steps_since_rest += 1
        self.stamina_lost_this_step = stamina_lost_this_step
        self.stamina -= self.stamina_lost_this_step
        self.fibonacci_sequence.append(self.stamina_lost_this_step)

    def reset(self):
        """
        Reset Fibonacci Frailty back to zero steps.
        """

        self.stamina_lost_this_step = 0
        self.steps_since_rest = 0
        self.fibonacci_sequence = deque(maxlen=2)
