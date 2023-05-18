#!/usr/bin.env python3

"""
This module provides the LRUCache class
"""

import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ A LRUCache class """

    time = datetime.datetime

    def __init__(self):
        """ Initialize instance """
        super().__init__()
        self.register = {}

    def put(self, key, value):
        """
        Assigns to the dictionary self.cache_data
        the item `value` for the key `key`
        """
        if key is None or value is None:
            return
        self.register[key] = self.time.utcnow()
        self.cache_data[key] = value
        if len(self.cache_data) > self.MAX_ITEMS:
            usage_history = list(self.register.values())
            usage_history.sort()
            removed = list(filter(lambda k: self.register[k] ==
                                  usage_history[0], self.register))[0]
            print('DISCARD:', removed)
            del self.register[removed]
            del self.cache_data[removed]

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return
        self.register[key] = self.time.utcnow()
        return self.cache_data.get(key)
