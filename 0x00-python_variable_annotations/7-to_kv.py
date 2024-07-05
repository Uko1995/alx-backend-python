#!/usr/bin/env python3
'''function takes returns tuple'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''retuns a tuple'''
    square: float = v**2
    return (k, square)
