#!/usr/bin/env python3
"""
Implement a method with two integer arguments, with default value of 10.
"""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''
        This initialize instance.
        '''
        self._dataset = None
        self._indexed_dataset = None

    def _load_dataset(self) -> List[List[str]]:
        '''
        This cache the dataset.
        '''
        if self._dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                self._dataset = [row for row in reader][1:]

        return self._dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        '''
        This dataset indexed by sorting position, starting at 0.
        '''
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self._indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
        This returns dictionary of pagination data.
        '''
        assert 0 <= index < len(self._load_dataset())

        indexed_dataset = self.indexed_dataset()
        indexed_page = {}

        i = index
        while len(indexed_page) < page_size and i < len(self._load_dataset()):
            if i in indexed_dataset:
                indexed_page[i] = indexed_dataset[i]
            i += 1

        page = list(indexed_page.values())
        page_indices = indexed_page.keys()

        return {
            'index': index,
            'next_index': max(page_indices) + 1,
            'page_size': len(page),
            'data': page
        }
