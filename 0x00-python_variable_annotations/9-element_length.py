#!/usr/bin/env python3
"""
annotated types
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence])\
      -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """annotated function element_length"""
    return [(i, len(i)) for i in lst]
