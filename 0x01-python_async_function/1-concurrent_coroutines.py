#!/usr/bin/env python3
"""Async function"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
