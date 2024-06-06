#!/usr/bin/env python3
"""A type-annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A function that takes in a list of
    integers and floats

    Args:
    mxd_lst: list of integers and float

    Return:
    Sum in float
    """

    return sum(mxd_lst)
