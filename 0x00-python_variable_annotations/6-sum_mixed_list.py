#!/usr/bin/env python3
"""
    type-annotated function sum_mixed_list which takes
    a list mxd_lst of integers and floats and returns
    their sum as a float.
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]])-> float:
    """takes a list mxd_lst of integers and floats and returns their sum as a float."""
    sum = 0
    for fi in mxd_lst:
        sum += fi
    return sum