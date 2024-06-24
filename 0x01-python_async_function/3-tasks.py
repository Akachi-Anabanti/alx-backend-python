#!/usr/bin/env python3
''' Async without async def'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> wait_random:
    ''' returns asyncio task '''
    return asyncio.Task(wait_random(max_delay))
