#!/usr/bin/env python3

"""
This provides the LFUCache class
"""

import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    time = datetime.datetime

    def __init__(self):
        """ Initialize instance """
        super().__init__()
        self.count_register = {}
        self.time_register = {}

    def put(self, key, value):
        """
        Assigns to the dictionary self.cache_data
        the item `value` for the key `key`
        """
        if key is None or value is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) > self.MAX_ITEMS - 1:
                count_history = list(self.count_register.values())
                count_history.sort()
                least_used = list(filter(lambda k: self.count_register[k] ==
                                         count_history[0],
                                         self.count_register))
                if len(least_used) > 1:
                    time_least_used = {k: v
                                       for k, v in self.time_register.items()
                                       if k in least_used}
                    time_history = list(time_least_used.values())
                    time_history.sort()
                    lru = time_history[0]
                    remove = list(filter(lambda k: self.time_register[k] ==
                                         lru, self.time_register))[0]
                else:
                    remove = least_used[0]
                print('DISCARD:', remove)
                del self.cache_data[remove]
                del self.count_register[remove]
                del self.time_register[remove]
        if key not in self.count_register.keys():
            self.count_register[key] = 1
        else:
            self.count_register[key] += 1
        self.cache_data[key] = value
        self.time_register[key] = self.time.utcnow()

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return
        self.count_register[key] += 1
        self.time_register[key] = self.time.utcnow()
        return self.cache_data.get(key)
