#!/usr/bin/env python3

"""
This module provides the function index_range
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    This function returns a tuple of size two containing a start
    index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    if not isinstance(page, int) or not isinstance(page_size, int):
        return
    end = page * page_size
    start = end - page_size
    indexRange = (start, end)

    return indexRange
