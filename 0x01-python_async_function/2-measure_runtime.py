#!/usr/bin/env python3
"""Python async function"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Function taht measures run time

    Args:
    n: int
    max_delay: int

    Returns
    Measured run time in float
    """
    start = time.perf_counter()
    # await wait_n(n, max_delay)
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total = end - start
    print(total)
    return total / n
