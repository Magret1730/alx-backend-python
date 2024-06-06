#!/usr/bin/env python3
""" A type-annotated function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function that takes in a str and int or float

    Args:
    k: a string
    v: integer or float

    Returns:
    tuple of string and float
    """

    return k, float(v ** 2)
