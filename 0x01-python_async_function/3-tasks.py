#!/usr/bin/env python3
"""
takes an integer max_delay and returns a asyncio.Task.
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an integer max_delay and returns a asyncio.Task"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    task = asyncio.create_task(wait_random(max_delay))

    return task
