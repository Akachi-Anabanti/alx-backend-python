#!/usr/bin/env python3
'''Executes an asyncio task without await'''
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''return a list of floats from delay values'''
    wait_times = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
            )
    return sorted(wait_times)
