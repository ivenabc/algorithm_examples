# -*- coding:utf-8 -*-

# 插入排序
class Insertion(object):
    def __init__(self, list):
        self.__list = list 
    
    def sort(self):
        length = len(self.__list)
        for i in range(1, length):
            for j in range(i, 0, -1):
                if self.less(j, j-1): self.exch(j, j-1)


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
    s = Insertion([5,4,3,1,2])

    s.sort()
    print(s.get_list())
