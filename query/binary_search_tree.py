# coding=utf-8

#二叉树查找
class Node:
    def __init__(self,key,value, n=1):
        # self.next = None
        self.left = None 
        self.right = None 
        self.key = key 
        self.value = value 
        self.n = n

class BinarySearchTree:
    def __init__(self):
        self.root = None
    

    @staticmethod
    def get_node(key, node):
        if not node: return None
        if node.key > key:
            return BinarySearchTree.get_node(key, node.left) 
        elif node.key < key:
            return BinarySearchTree.get_node(key, node.right) 
        else:
            return node

    @staticmethod
    def size_node(node):
        if node == None:
            return 0
        else:
            return node.n
    
    @staticmethod
    def put_node(node, key, value):
        if not node: return Node(key, value)
        
        if node.key > key:
            node.left = BinarySearchTree.put_node(node.left, key, value)
        elif node.key < key:
            node.right = BinarySearchTree.put_node(node.right, key, value)
        else:
            node.value = value 
        
        node.n = BinarySearchTree.size_node(node.left) + BinarySearchTree.size_node(node.right) + 1
        return node

    @staticmethod
    def min_node(node):
        if not node.left: return node
        return BinarySearchTree.min_node(node.left)
    
    @staticmethod
    def select_node(node, k):
        if not node: return None
        t = BinarySearchTree.size_node(node.left)
        if t > k:
            return BinarySearchTree.select_node(node.left, k)
        elif t < k:
            return BinarySearchTree.select_node(node.right, k-t-1)
        else:
            return node 
    
    @staticmethod
    def delete_min_node(node):
        if not node.left: return node.right
        x.left = BinarySearchTree.delete_min_node(ndoe.left) 
    
    @staticmethod
    def delete_node(node, key):
        if not node: return None
        if key > node.key:
            node.right = BinarySearchTree.delete_node(node.right, key)
        elif key < node.key:
            node.left = BinarySearchTree.delete_node(node.left, key)
        else:
            if not node.right: return node.left 
            if not node.left: return node.right
            t = node 
            node = min(t.right)
            node.right = BinarySearchTree.delete_min_node(node.right)
            node.left = t.left
    
    def delete(self,key):
        self.root = BinarySearchTree.delete_node(self.root, key)


    def delete_min():
        self.root = BinarySearchTree.delete_min_node(self.root)

    def select(self, k):
        return BinarySearchTree.select_node(self.root, k)
    
    def min(self):
        return BinarySearchTree.min_node(self.root)


    def put(self, key, value):
        self.root = BinarySearchTree.put_node(self.root, key, value)

    def get(self, key):
        return BinarySearchTree.get_node(key, self.root)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.put('h', 0)
    bst.put('k', 2)
    bst.put('c', 4)
    bst.put('d', 5)

    print(bst.get('d').n)
    print(bst.select(1).key)
    print(bst.min().key)
    bst.delete('k')
    print(bst.get('k'))