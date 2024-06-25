#!/usr/bin/env python3
''' A script that defines a coroutine'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''async function that awaits a sleep'''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
