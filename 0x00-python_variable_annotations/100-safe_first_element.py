#!/usr/bin/env python3
"""
annotating function
"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any])\
     -> typing.Union[typing.Any, None]:
    """annotated function"""
    if lst:
        return lst[0]
    else:
        return None
