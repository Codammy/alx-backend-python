#!/usr/bin/env python3
"""
    type-annotated function sum_list which takes
    a list input_list of floats as argument and
    returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of input_list"""
    sum = 0.0
    for f in input_list:
        sum += f
    return sum
