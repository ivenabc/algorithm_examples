#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## SortTemplate

class SortTemplate(object):

    def __init__(self, list):
        self.list = list 
    
    def sort(self):
        pass
    
    def less(self, i, j):
        return self.list[i] < self.list[j]
    
    def exch(self, i, j):
        self.list[i], self.list[j] = self.list[j], self.list[i]
    
    def show(self):
        print(self.list)
    
    def is_sorted(self):
        for i in range(1, len(self.list)):
            if(self.less(i, i-1)):
                return False
    

class Father():
    def __init__(self):
        self.a='aaa'
    def action(self):
        print('调用父类的方法')
    
    def hello(self):
        print(self.a)
 
class Son(Father):
    def __init__(self):
        self.a='bbb'
    def action(self):
        print('子类重写父类的方法')


if __name__ == '__main__':
    # s = SortTemplate
    # print(dir(s))
    son=Son()
    # son.action()
    print(son.hello())