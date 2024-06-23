#!/usr/bin/env python3
'''Duck typing for a sequence'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' returns an item or none'''
    if lst:
        return lst[0]
    else:
        return None
