#!/usr/bin/env python3
"""
    an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random
    n times with the specified max_delay.
"""
import asyncio
import typing
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """return the list of all the delays (float values)."""
    waits = [await wait_random(max_delay) for i in range(n)]
    custom_sort(waits)
    return waits


def custom_sort(lst: typing.List[float]) -> None:
    """custom sort function implementing bubble sort alg"""
    for pos in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
