#!/usr/bin/env python3
'''Correctly annotates a function and it's return values'''
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns a list of tuple of sequence and int'''
    return [(i, len(i)) for i in lst]
