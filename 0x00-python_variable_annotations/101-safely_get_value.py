#!/usr/bin/env python3
'''Safely get any type with typevar'''
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping,
        key: Any, 
        default: Union[T, None] = None) -> Union[Any, T]:
    ''' returns typevars'''
    if key in dct:
        return dct[key]
    else:
        return default
