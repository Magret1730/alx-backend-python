#!/usr/bin/env python3
"""An async function"""
from typing import Awaitable
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[float]:
    """Function that returns asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
