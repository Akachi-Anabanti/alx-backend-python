#!/usr/bin/env python3
''' A script that defines a coroutine'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''async function that awaits a sleep'''
    val = random.uniform(0, 10)
    await asyncio.sleep(val)
    return val
