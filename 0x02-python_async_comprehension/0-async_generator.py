#!/usr/bin/env python
'''coroutine function'''
import asyncio
import random


async def async_generator():
    '''async_generator function'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
