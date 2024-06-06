#!/usr/bin/env python3
""" Annotating an already defined function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that takes an iterable of sequences and returns a list of tuples
    Each tuple contains a sequence from the input iterable and its length.

    Args:
    lst: An iterable containing sequences.

    Returns:
    A list of tuples where each tuple contains a sequence and its length.
    """
    """
    Iterable[Sequence] indicates that lst can be any iterable
    (e.g., list, tuple, set) containing sequences.
    A Sequence can be any object that supports sequence operations,
    like strings, lists, or tuples
    """

    return [(i, len(i)) for i in lst]
