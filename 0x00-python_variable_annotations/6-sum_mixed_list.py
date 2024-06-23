#!/usr/bin/env python3
'''A script that defines a function sum_mixed_list
which is a list of mixed float, integers and returns the
sum'''
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''returns the sum of mxd_list'''
    return sum(mxd_list)
