#!/usr/bin/env python3
'''function returns an async task'''
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''function that returns an async task'''
    return asyncio.create_task(wait_random(max_delay))
