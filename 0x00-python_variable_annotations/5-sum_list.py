#!/usr/bin/env python3
'''function takes a list o floats and returns their sum as float'''
from typing import List

def sum_list(input_list: List[float]) -> float:
    '''returns the sum as float'''
    sumList: float = 0.0
    for item in input_list:
        sumList += item

    return sumList
