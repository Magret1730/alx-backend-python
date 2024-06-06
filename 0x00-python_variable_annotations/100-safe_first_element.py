#!/usr/bin/env python3
"""An already defined function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    A function that returns the first element of a sequence if
    it exists, otherwise None.

    Args:
    lst: A sequence containing elements of any type.

    Returns:
    The first element of the sequence if it exists, otherwise None.
    """

    if lst:
        return lst[0]
    else:
        return None
