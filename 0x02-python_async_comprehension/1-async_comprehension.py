#!/usr/bin/env python3
'''create async coroutine that uses async comprehension'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''async_comprehension coroutine'''
    numbers = [num async for num in async_generator()]
    return numbers
