#!/usr/bin/env python3
"""
A class FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    This defines FIFOCache
    '''

    def __init__(self):
        '''
        This initializes FIFOCache
        '''
        super().__init__()

    def put(self, key, item):
        '''
        This assigns the item to the dictionary
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # FIFO eviction: Discard the first item put in cache
                discarded_key = next(iter(self.cache_data))
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
