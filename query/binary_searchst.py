# -*- coding:utf-8 -*-

#二分查找法

class Node:
    def __init__(self,key,value):
        # self.next = None
        self.key = key 
        self.value = value 

class BinarySearchST:
    def __init__(self):
        self.list = []
    
    def rank(self, key):
        start = 0 
        end = len(self.list)
        if end == 0:
            return 0
        while start <= end:
            mid = start +  (end - start)//2
            node = self.list[mid]
            if node.key > key:
                end = mid - 1
            elif node.key < key:
                start = mid + 1
            else: 
                return mid
        return start

    def put(self, key, value):
        index = self.rank(key)
        print(index)
        node = Node(key, value)
        self.list.insert(index, node)
    
    def get(self, key):
        index = self.rank(key)
        if index < len(self.list):
            return self.list[index]
        return None
    
    def delete(self, key):
        index = self.rank(key)
        if index < len(self.rank):
            self.list.pop(index)
    
    # def contains(self, key):
    #     return key in self.dict
    
    def is_empty(self):
        return len(self.list) == 0
    
    def size(self):
        return len(self.list)


if __name__ == '__main__':
    bst = BinarySearchST()
    bst.put('k', 2)
    bst.put('a', 4)
    bst.put('d', 5)

    print(bst.list[0].key, bst.list[1].key, bst.list[2].key)