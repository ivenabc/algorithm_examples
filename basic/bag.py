#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Bag

class Bag(object):
    def __init__(self):
        self.__list =[]
    
    def add(self, item):
        self.__list.append(item)

    def is_empty(self):
        return bool(self.__list)
    
    def size(self):
        return len(self.__list)

    def __iter__(self):
            self.__iter_index = 0 
            return self 
    
    def __next__(self):
        if len(self.__list) <= self.__iter_index:
            raise StopIteration
        else:
            value = self.__list[self.__iter_index]
            self.__iter_index += 1
            return value
    
if __name__ == '__main__':
    bag = Bag()
    bag.add(1)
    if bag.is_empty():
        bag.add(2)
    
    sum = 0
    for val in bag:
        sum += val
    
    print(sum)