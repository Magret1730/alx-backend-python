#!/usr/bin/env python3
"""Task 0 solution"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Caroutine that loops 10 times each time async
    wait 1 sec and then yield a random number
    between 0 and 10
    """
    # Generator[yield_type, send_type, return_type]

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
