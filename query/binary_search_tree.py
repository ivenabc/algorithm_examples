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
        self.root = Node('default', 1)
    

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

    def put(self, key, value):
        self.root = BinarySearchTree.put_node(self.root, key, value)

    def get(self, key):
        return BinarySearchTree.get_node(key, self.root)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.put('k', 2)
    bst.put('a', 4)
    bst.put('d', 5)

    print(bst.get('a').n)