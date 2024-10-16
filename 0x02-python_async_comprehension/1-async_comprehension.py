#!/usr/bin/env python3
"""
    This coroutine will collect 10 random numbers
    using an async comprehensing over async_generator,
    then return the 10 random numbers.
"""
import typing


async def async_comprehension() -> typing.List[float]:
    """async_comprehension that takes no arguments"""
    async_generator = __import__("0-async_generator").async_generator
    random_10 = [i async for i in async_generator()]
    return random_10
