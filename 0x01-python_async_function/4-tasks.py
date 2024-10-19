#!/usr/bin/env python3
"""

"""
import typing
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """return the list of all the delays (float values)."""
    waits = [await task_wait_random(max_delay) for i in range(n)]
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
