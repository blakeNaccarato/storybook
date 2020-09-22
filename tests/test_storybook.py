"""
Tests.
"""

import storybook


def test_ch1():
    """
    Check Chapter 1.
    """

    correct_health = storybook.Mage.INITIAL_HEALTH - sum(storybook.CH1_DAMAGE_EACH_STEP)

    mage = storybook.ch1(storybook.Mage())
    assert mage.health == correct_health
