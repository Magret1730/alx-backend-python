#!/usr/bin/env python3
"""An annotted type function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A function that takes in list of floats

    Args:
    input_list - list of float

    Return:
    sum in float
    """

    return sum(input_list)
