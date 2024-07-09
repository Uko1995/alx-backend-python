#!/usr?bin/env python3
''' runs wait_random() n times and returns a list of the delays'''
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''wait_n function'''
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    result = await asyncio.gather(*tasks)
    return result
