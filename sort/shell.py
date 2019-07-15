
# -*- coding:utf-8 -*-

# 希尔排序
class Shell(object):
    def __init__(self, list):
        self.__list = list 
    
    def sort(self):
        N = len(self.__list)
        h = 1
        while h < N/3: 
            print('h:', h)
            h=3*h+1
        while h >= 1:
            for i in range(h, N):
                for j in range(i, h-1, -h):
                    if self.less(j, j-h):   self.exch(j, j-h)
            h = h//3
        # length = len(self.__list)
        # for i in range(1, length):
        #     for j in range(i, 0, -1):
        #         if self.less(j, j-1): self.exch(j, j-1)


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
    s = Shell([5,4,3,1,2,3,4,9,7,5,9,6,8])

    s.sort()
    print(s.get_list())
