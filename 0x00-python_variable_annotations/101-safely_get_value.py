#!/usr/bin/env python3
"""Annotated safely_get_value function"""
from typing import Mapping, Any, Union, TypeVar

# Define a type variable for the return type
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None])\
                     -> Union[Any, T]:
    """
    A function that safely gets a value from a dictionary.

    Args:
    dct: A mapping (e.g., dict) from keys to values.
    key: The key whose value to retrieve from the dictionary.
    default: The default value to return if the key is not found
    in the dictionary. Defaults to None.

    Returns:
    The value associated with the key if it exists in the dictionary,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
