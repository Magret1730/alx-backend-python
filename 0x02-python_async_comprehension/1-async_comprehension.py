#!/usr/bin/env python3
"""Task 1 solution"""
from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async coprehension function that takes in
    10 random numbers

    Returns:
    the 10 random numbers
    """

    return [i async for i in async_generator()]
