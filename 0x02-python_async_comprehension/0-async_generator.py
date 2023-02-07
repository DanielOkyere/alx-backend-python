#!/usr/bin/env python3
"""
Coroutine to loop 10 times asynchronously wait 1 second
then yield random number between 0 and 10.
"""
import random
import asyncio
from typing import Generator


def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times and yields a random number between 0 and 10
    """
    for in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
