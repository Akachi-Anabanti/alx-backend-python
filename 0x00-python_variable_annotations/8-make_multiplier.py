#!/usr/bin/env python3
'''Defines a function that takes a callable
and args'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by multiplier'''
    def func(value: float) -> float:
        '''multiplies a float [value] by mulitplier'''
        return value * multiplier
    return func
