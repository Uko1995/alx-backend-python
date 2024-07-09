#!/usr/bin/env python3
'''function thata tasks integer, waits for a random delay and returns it'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''aync coroutine function'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
