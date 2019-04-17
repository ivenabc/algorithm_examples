#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Stack
#后进先出，LIFO 栈

class Stack(object):
    def __init__(self):
        self.__list = []
        self.__iter_index =0
    
    def push(self, item):
        if self.__list:
           self.__list.append(item)
        else:
            self.__list.insert(0, item)
    
    def pop(self):
        self.__list.pop(1)

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
    pass