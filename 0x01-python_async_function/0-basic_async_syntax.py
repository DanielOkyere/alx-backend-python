#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Async coroutine that takes an integer argument
    Args:
        max_delay(int) delay coroutine

    Return:
        random value(float)
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
