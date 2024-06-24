#!/usr/bin/env python3
'''Executes an asyncio task without await'''
from typing import List

task_wait_random = __import__('3-task').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''return a list of floats from delay values'''
    result = []
    for _ in range(max_delay):
        val = await task_wait_random(max_delay)
        result.append(val)
    return result
