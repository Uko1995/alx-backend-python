#!/usr/bin/env python3
'''Runs wait_random() n times and returns a list of the delays'''
import asyncio
import heapq
from typing import List

# Import the task_wait_random function from the previous task
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Wait_n function'''
    heap = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Run all tasks concurrently and collect results
    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(heap, delay)

    return [heapq.heappop(heap) for _ in range(len(heap))]
