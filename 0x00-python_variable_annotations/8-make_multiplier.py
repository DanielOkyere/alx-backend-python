#!/usr/bin/env python3
"""
Complex types functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make multiplier takes a float as argument and returns a float function that
    """

    def multiplier_func(number: float) -> float:
        """
        Multiplies a float by multipler
        """
        return multiplier * number

    return multiplier_func
