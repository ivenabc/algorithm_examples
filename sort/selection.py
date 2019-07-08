#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sort_template import  SortTemplate

## Selection
class Selection(object):
    """
    选择排序：首先找到数组中最小得元素,其次将它和数组得第一个元素交换位置。
    再次在剩下得元素中找到最小得位置，将它与数组中第二个元素交换位置。如此往复，直到将整个数组排序

    每进行一次交换和N-1-i次比较，因此总共有N次交换以及(N-1) + (N-2) + ... + 2 + 1 = N(N-1)/2 ~ N**2/2
    """
    def __init__(self,list):
        self.__list = list
    
    def sort(self):
        length = len(self.__list)

        for i in range(length):
            min = i 
            for j in range (i+1, length):
                if (self.less(j, min)): min = j 
            self.exch(i, min)
    
    
    
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
    
    def get_list(self):
        return self.__list
    
if __name__ == '__main__':
    s = Selection([5,3,1,2,4])
    s.sort()
    print(s.get_list())