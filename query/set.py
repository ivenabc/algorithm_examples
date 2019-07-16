
class Node:
    def __init__(self,key):
        self.next = None
        self.key = key 
        # self.pref 

class Set(object):
    def _init_(self):
        self.dict = {}
    
    def put(self, key, value):
        self.dict[key] = value
    
    def get(self, key):
        return self.dict.get(key, default='default')
    
    def delete(self, key):
        self.dict.pop(key, default='default')
    
    def contains(self, key):
        return key in self.dict
    
    def is_empty(self, key):
        return len(self.dict) == 0
    
    def size(self):
        return len(self.dict)
    
    