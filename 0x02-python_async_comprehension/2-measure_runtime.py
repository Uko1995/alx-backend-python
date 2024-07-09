#!/usr/bin/env python3
'''coroutine to measure excution time'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures execution time'''
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    execution_time = time.perf_counter() - start_time
    return execution_time
