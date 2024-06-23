#!/usr/bin/env python3
''' Mypy check and fix'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    ''' returns a list of  itmes from lst'''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
