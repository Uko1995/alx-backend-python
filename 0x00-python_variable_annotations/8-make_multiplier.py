#!/usr/bin/env python3
'''function takes a float and multiplies by the float'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''function returns a function'''
    def multiplier_function(value: float) -> float:
        ''' returns a float multiplied by multiplier'''
        return value * multiplier
    return multiplier_function
