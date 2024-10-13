#!/usr/bin/env python3
"""
type annotations
"""
import typing
T = typing.TypeVar("T")


def safely_get_value(dct: typing.Mapping,
                     key: typing.Any,
                     default: typing.Union[T, None] = None)\
                          -> typing.Union[None, T]:
    """type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
