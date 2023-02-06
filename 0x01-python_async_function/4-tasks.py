#!/usr/bin/env python3
"""
Method that spawns n times with specific delay to call
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times
    Args:
        n: int, number of times to spawn wait_random
    Returns:
        list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
