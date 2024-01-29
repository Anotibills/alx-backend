#!/usr/bin/env python3
"""
A function that takes two integer arguments and returns tuple
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    This returns  indexes in a list for pagination parameters.
    '''
    return ((page - 1) * page_size, page * page_size - 1)
