#!/usr/bin/env python3
'''annotate the function below'''
from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''retuns a tuple'''
    return [(i, len(i)) for i in lst]
