#!/usr/bin/env python3
"""
    measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n
"""
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - s) / n
