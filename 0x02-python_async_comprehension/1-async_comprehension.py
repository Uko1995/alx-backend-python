#!/usr/bin/env python3
'''create async coroutine that uses async comprehension'''
import random
import asyncio
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[List[float], None, None]:
    '''async_comprehension coroutine'''
    numbers = [num async for num in async_generator()]
    return numbers
