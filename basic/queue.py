#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Queue
# 先进先出队列(FIFO)

class Queue(object):
    def __init__(self):
        self.__list = []
    
    # 添加一个元素
    def en_queue(self, item):
        self.__list.append(item)
    
    # 删除最近添加的元素
    def de_queue(self):
        self.__list.pop()

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