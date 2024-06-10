#!/usr/bin/env python3
"""Task 4"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n function

    Args:
    n: int
    max_delay: int

    Return:
    list of sorted delays
    """

    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
