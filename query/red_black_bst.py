#coding:utf-8

class Node:
    __init__(self, key, value, color, size):
        self.key = key 
        self.value = value 
        self.color = color 
        self.size = size 

    
    def size(self):
        return self.size 

    # def is_empty(self):
    #     return 


class RedBlackBST:
    def put(self, key, value):
        self.root = RedBlackBST.put_node(self.root, key, value)
    
    def get(self, key):
        x = self.root
        while x :
            if key < x.key: x = x.left 
            elif key > x.key: x = x.right 
            else: return x.value
        return None

    def contains(self, key):
        return self.get(key) != None
    
    def balance(node):
        if RedBlackBST.is_red(node.right): node = RedBlackBST.rotate_left(node)
        if RedBlackBST.is_red(node.left) and RedBlackBST.is_red(node.left.left): node = RedBlackBST.rotate_right(node)
        if RedBlackBST.is_red(node.left) and RedBlackBST.is_red(node.right): RedBlackBST.flip_colors(node)
        node.size = RedBlackBST.size(node.left) + RedBlackBST.size(node.right) + 1
        return node
    
    @staticmethod
    def delete_min_node(node):
        if not node.left: return None 
        # if RedBlackBST.is_red

    @staticmethod
    def put_node(self, node, key, value):
        if not node: return Node(key, value, True, 1)
        
        if key < node.key: node.left = put(node.left, key, value)
        elif key > node.key: node.right = put(node.right, key, value)
        else node.value = value

        if RedBlackBST.is_red(node.right) and !RedBlackBST.is_red(node.left):  node = RedBlackBST.rotate_left(node)
        if RedBlackBST.is_red(node.left) and RedBlackBST.is_red(node.left.left): node = RedBlackBST.rotate_right(node)
        if RedBlackBST.is_red(node.left) and RedBlackBST.is_red(node.right): RedBlackBST.flip_colors(node)
        
        node.size = RedBlackBST.size(node.left) + RedBlackBST.size(node.right) + 1
        return node 

    @staticmethod
    def rotate_left(node):
        x = node.right
        node.right = x.left 
        x.left = node 
        x.color = x.left.color 
        x.left.color = True
        x.size = node.size 
        node.size = RedBlackBST.size(node.left) + RedBlackBST.size(node.right) + 1 
        return x 

    @staticmethod
    def rotate_right(node):
        x = node.left 
        node.left = x.right 
        x.right = node 
        x.color = x.right.color 
        x.right.color = True
        x.size = node.size 
        node.size = RedBlackBST.size(node.left) + RedBlackBST.size(node.right) + 1 
        return x  

    @staticmethod
    def size(node):
        if not node: return 0 
        return node.size 
    
    @staticmethod
    def is_red(node):
        if not node: return False
        return x.color
    
    @staticmethod
    def flip_colors(node):
        node.color = !node.color 
        node.left.color = !node.left.color 
        node.right.color = !node.right.color 