#!/bin/usr/env python3

"""
This module provides the class FIFOCache
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A FIFOCache class """

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
            self.register.append(key)
            self.cache_data[key] = value
            if len(self.cache_data) > self.MAX_ITEMS:
                removed = self.register[0]
                print('DISCARD:', removed)
                del self.cache_data[removed]
                del self.register[0]
        else:
            self.cache_data[key] = value

    def get(self, key):
        """
        Return the value in self.cache_data
        linked to key
        """
        return self.cache_data.get(key, None)
