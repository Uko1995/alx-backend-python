#!/usr/bin/env python3
''' annotate the function below'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' returns list'''
    if lst:
        return lst[0]
    else:
        return None
