#!/usr/bin/env python3
"""
    execute async_comprehension four times in
    parallel using asyncio.gather
"""
import time
import asyncio


async def measure_runtime() -> float:
    async_c = __import__("1-async_comprehension").async_comprehension
    t = time.perf_counter()
    await asyncio.gather(async_c(), async_c(), async_c(), async_c())
    return time.perf_counter() - t
