#!/usr/bin/env python3
'''Runs wait_random() n times and returns a list of the delays'''
import asyncio
import heapq
from typing import List

# Import the wait_random function from the previous task
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Wait_n function'''
    heap = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Run all tasks concurrently and collect results
    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(heap, delay)

    return [heapq.heappop(heap) for _ in range(len(heap))]


if __name__ == "__main__":
    n = 5
    max_delay = 10
    result = asyncio.run(wait_n(n, max_delay))
    print(result)

