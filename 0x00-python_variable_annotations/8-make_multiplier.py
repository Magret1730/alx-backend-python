#!/usr/bin/env python3
"""A type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that takes a loat and returns a function

    Args:
    multiplier: float

    Returns:
    a function that takes a float and returns a float
    """

    def multiplier_function(value: float) -> float:
        """
        The return function

        Arg:
        value: argument value in float

        Returns:
        value multiplied my multiplier in float
        """

        return value * multiplier

    return multiplier_function
