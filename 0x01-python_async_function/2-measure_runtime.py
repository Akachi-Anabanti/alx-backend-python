#!/usr/bin/env python3
'''Measures the execution time of a coroutine'''
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''measures the time of wait_n / n'''
    start = time.time()
    await wait_n(n, max_delay)
    return (time.time() - start) / float(n)
