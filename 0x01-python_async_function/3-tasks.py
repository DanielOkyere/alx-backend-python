#!/usr/bin/env python3
"""
Method to return a task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a task that waits for a random number of seconds
    Args:
        max_delay: max num of seconds
    """
    return asyncio.create_task(wait_random(max_delay))
