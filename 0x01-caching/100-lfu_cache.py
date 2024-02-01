#!/usr/bin/env python3
"""
A class LFUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    '''
    This defines LFUCache
    '''

    def __init__(self):
        '''
        This initializes LFUCache
        '''
        super().__init__()
        self.freq_counter = {}

    def put(self, key, item):
        '''
        This assigns the item to the dictionary
        '''
        if key is None or item is None:
            return
        if key in self.freq_counter:
            self.freq_counter[key] += 1
        else:
            self.freq_counter[key] = 1
        self.cache_data[key] = item
        if len(self.cache_data) >= self.MAX_ITEMS:
            least_freq_keys = [k for k, v in self.frequency.items()
                               if v == min(self.frequency.values())]
        if len(lfu_items) > 1:
            lru_key = min(self.cache_data, key=lambda k: self.cache_data[k]['time'])
            lfu_items = [lru_item]

        for lfu_item in lfu_items:
            del self.cache_data[lfu_item]
            del self.freq_counter[lfu_item]
            print("DISCARD:", lfu_item)

    def get(self, key):
        '''
        This returns the value associated with the given key
        '''
        if key is None or key not in self.cache_data:
            return None

        self.freq_counter[key] += 1

        return self.cache_data[key]
