#!/usr/bin/env python3
"""Already defined function"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    A function that takes in tuple

    Args:
    lst
    factor

    Returns:
    list of integers
    """

    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Using tuple instead of list for array

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
