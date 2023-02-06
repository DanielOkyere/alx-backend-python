#!/usr/bin/env python3
"""
Lets execute multiple coroutines at the same time
with async
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawsn wait_random n number of times
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    result = []
    for n in range(n):
        result.append(await wait_random(max_delay))

    return result
