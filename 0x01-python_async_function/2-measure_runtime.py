#!/usr/bin/env python3
'''function that measures the total execution time for wait_n()'''
import random
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''function measures total execution time
        Args: n(int), max_delay(int)
        returns: total_time/n
    '''
    beginning = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - beginning
    return total_time / n
