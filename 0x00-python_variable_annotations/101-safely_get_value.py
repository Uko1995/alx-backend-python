#!/urs/bin/env python3
'''annotate the function below'''
from typing import Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(
                     dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''function returns dict'''
    if key in dct:
        return dct[key]
    else:
        return default
