#!/usr/bin/env python3
""" Async function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random is a function

    Args:
    max_delay: int

    Returns:
    float
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
