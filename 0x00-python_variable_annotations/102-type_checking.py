#!/usr/bin/env python3
"""Already defined function"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """
    A function
    """

    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Using tuple instead of list for array

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
