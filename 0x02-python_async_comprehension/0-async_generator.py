#!/usr/bin/env python3
"""Task 0 solution"""
from typing import List
import asyncio
import random


async def async_generator() -> List[float]:
    """
    Caroutine that loops 10 times each time async
    wait 1 sec and then yield a random number
    between 0 and 10
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
