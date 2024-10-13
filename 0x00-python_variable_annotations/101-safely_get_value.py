#!/usr/bin/env python3
"""
type annotations
"""
import typing


def safely_get_value[T](dct: typing.Mapping, key: typing.Any, default = None):
    """type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default