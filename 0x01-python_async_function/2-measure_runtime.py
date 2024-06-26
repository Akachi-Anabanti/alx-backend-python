#!/usr/bin/env python3
'''Measures the execution time of a coroutine'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measures the time of wait_n / n'''
    start = time.time()
    asyncio.Task(wait_n(n, max_delay))
    return (time.time() - start) / float(n)
