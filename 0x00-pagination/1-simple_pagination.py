#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer arguments
"""
import csv
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    '''
    This class serves to paginate a database of popular baby names.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''
        This initialize instance.
        '''
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        '''
        This returns the cached dataset.
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                self.__dataset = [row for row in reader][1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        '''
        This returns output page of dataset.
        '''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)

        return self.dataset()[start:end] if start < len(self.dataset()) else []
