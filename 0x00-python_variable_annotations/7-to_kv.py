#!/usr/bin/env python3
"""
    type-annotated function to_kv that takes a string k
    and an int OR float v as arguments and returns a tuple
"""
import typing


def to_kv(k: str, v: typing.Union[list, float]) -> typing.Tuple[str, float]:
    """type annotated function"""
    return (k, v**2)
