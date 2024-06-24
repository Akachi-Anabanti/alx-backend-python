#!/usr/bin/env python3
'''A couroutine that generates random integers'''
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    '''async genrator generates random unifrm numbers'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
