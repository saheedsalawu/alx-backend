#!/bin/usr/env python3

"""
This module provides the class LIFOCache
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A LIFOCache class """

    def __init__(self):
        """ Initialize instance """
        super().__init__()
        self.register = []

    def put(self, key, value):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or value is None:
            return
        if key not in self.register:
            self.cache_data[key] = value
            if len(self.cache_data) > self.MAX_ITEMS:
                removed = self.register.pop()
                print('DISCARD:', removed)
                del self.cache_data[removed]
            self.register.append(key)
        else:
            self.cache_data[key] = value

    def get(self, key):
        """
        Return the value in self.cache_data
        linked to key
        """
        return self.cache_data.get(key, None)
