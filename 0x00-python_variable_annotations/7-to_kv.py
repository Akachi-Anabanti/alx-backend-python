#!/usr/bin/env python3
'''Defines a function to_kv that takes a string and an int
or float v as arguments and returns a tuple'''
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple of k and v'''
    return (k, v**2)
