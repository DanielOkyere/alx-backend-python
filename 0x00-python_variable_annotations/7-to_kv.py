#!/usr/bin/env python3
"""
Complex types-string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Converts a Python variable into a KV pair
    """
    return k, v ** 2
