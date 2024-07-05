#!/usr/bin/env python3
'''function takes a list of floats and
    integers and returns their sum as float'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    '''returns the sum as float'''
    sumList: float = 0.0
    for item in mxd_list:
        sumList += item

    return sumList
