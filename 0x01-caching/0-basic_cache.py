#!/bin/usr/env python3

"""
This module provides the class base_cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """

    def __init__(self):
        """ Initialize instance """
        super().__init__()

    def put(self, key, value):
        """
        Assigns to the dictionary self.cache_data
        the item `value` for the key `key`
        """
        if key is None or value is None:
            return
        self.cache_data[key] = value

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
