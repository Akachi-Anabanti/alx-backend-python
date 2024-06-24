#!/usr/bin/env python3
'''Executing multiple coroutines'''
from typing import List

wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return a list of floats from delay values'''
    return [await wait_random(max_delay) for _ in range(n)]
