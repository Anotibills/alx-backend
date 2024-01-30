#!/usr/bin/env python3
"""
A class LIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    This define LIFOCache
    '''

    def __init__(self):
        '''
        This initializes LIFOCache
        '''
        super().__init__()

    def put(self, key, item):
        '''
        This assigns the item to the dictionary
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # LIFO eviction: Discard the last item put in cache
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

            self.cache_data[key] = item

    def get(self, key):
        '''
        This returns the value associated with the given key
        '''
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
