#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Selection

class Selection(object):
    
    def __init__(self):
        self.__list = []
    
    def sort(self):
        pass
    
    def less(self, i, j):
        return self.__list[i] < self.__list[j]
    
    def exch(self, i, j):
        self.__list[i], self.__list[j] = self.__list[j], self.__list[i]
    
    def show(self):
        print(self.__list)
    
    def is_sorted(self):
        for i in range(1, len(self.__list)):
            if(self.less(i, i-1)):
                return False
    
