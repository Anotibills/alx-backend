#!/usr/bin/env python3
"""
A class BasicCache that inherits from BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    This defines a caching system with LRU eviction policy
    '''

    def put(self, key, item):
        '''
        This assigns the item to the dictionary
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        This returns the value associated with the given key
        '''
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
