"""
One possible solution to the Story of a Mage.
"""

from collections import deque


class Mage:
    """
    A mage on a journey.
    """

    def __init__(self):

        self.health = 100
        self.stamina = 150
        self.condition = None
        self.purse = {"gold": 2, "silver": 40}  # coin type: quantity
        self.pouch = {"pemmican": 1}  # item: quantity
        self.spells = {"Restore Stamina": 50, "Ranged Reach": 20}  # spell: cooldown

        self.contract(Healthy)

    def contract(self, condition):
        """
        Become afflicted with a condition.
        """

        self.condition = condition(self)

    def step(self):
        """
        Take a step.
        """

        self.condition.step()


class Healthy:
    """
    Do nothing on step when healthy.
    """

    def __init__(self, target):

        self.target = target

    def step(self):
        """
        Do nothing.
        """

        pass


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


# * ------------------------------------------------------------------------------ # *
# * EARLIER IMPLEMENTATIONS * #


class FibonacciFrailtyOld:
    """
    Reduce the mage's stamina for each step taken, according to the Fibonacci sequence.
    """

    def __init__(self, stamina):

        self.stamina = stamina
        self.stamina_lost_this_step = None
        self.steps_since_rest = None
        self.fibonacci_sequence = None
        self.reset()

    def __repr__(self):
        """
        Print the result of the latest step.
        """

        return (
            f"Steps taken: {self.steps_since_rest:3},"
            f" Stamina lost this step: {self.stamina_lost_this_step:3},"
            f" Stamina left: {self.stamina:3}."
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

        stamina_lost_this_step = sum(fibonacci_sequence)
        stamina -= stamina_lost_this_step
        fibonacci_sequence.append(stamina_lost_this_step)

        print(
            f"He has taken {steps_since_rest} steps,"
            f" lost {stamina_lost_this_step} stamina this step,"
            f" and has {stamina} stamina left."
        )

    if stamina > 0:
        #! Generalized "bench" out of this statement
        print("The mage has made it to his destination.\n")
    else:
        print("The mage is out of stamina. He spirals inward and collapses.\n")

    return stamina
