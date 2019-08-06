#coding:utf-8

class Node:
    def __init__(self, key, value, color, size):
        self.key = key 
        self.value = value 
        self.color = color 
        self.size = size
        self.right = None
        self.left = None

    
    def size(self):
        return self.size 

    # def is_empty(self):
    #     return 


class RedBlackBST:
    def __init__(self):
        self.root = None 

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
    
    def delete_min(self):
        if not self.root: return 
        if (not RedBlackBST.is_red(self.root.left)) and (not RedBlackBST.is_red(self.root.right)):
            self.root.color = True 
        self.root = RedBlackBST.delete_min_node(self.root)
        if self.root: self.root.color = False 
    
    def delete_max(self):
        if not self.root: return 
        if (not RedBlackBST.is_red(self.root.left)) and (not RedBlackBST.is_red(self.root.right)):
            self.root.color = True 
        self.root = RedBlackBST.delete_max_node(self.root)
        if self.root: self.root.color = False 
    
    def delete(self, key):
        if not self.get(key): return 
        if (not RedBlackBST.is_red(self.root.left)) and (not RedBlackBST.is_red(self.root.right)):
            self.root.color = True
        self.root = RedBlackBST.delete_node(self.root, key)
        if self.root: self.root.color = False 
    
    @staticmethod
    def min_node(node):
        if node.left == None: return node 
        else: return RedBlackBST.min_node(node.left)

    @staticmethod
    def delete_node(node, key):
        if key < node.key:
            if (not RedBlackBST.is_red(node.left)) and (not RedBlackBST.is_red(node.left.left)):
                node = RedBlackBST.move_red_left(node)
            node.left = RedBlackBST.delete_node(node.left, key)
        else:
            if RedBlackBST.is_red(node.left):
                node = RedBlackBST.rotate_right(node)
            if key == node.key and node.right == None:
                return None
            if (not RedBlackBST.is_red(node.right)) and (not RedBlackBST.is_red(node.right.left)):
                node = RedBlackBST.move_red_right(node)
            if key == node.key:
                x = RedBlackBST.min(node.right)
                node.key = x.key 
                node.value = x.value 
                node.right = RedBlackBST.delete_min(node.right)
            else: node.right = RedBlackBST.delete_node(node.right, key)
        return RedBlackBST.balance(node)

    @staticmethod
    def delete_max_node(node):
        if RedBlackBST.is_red(node.left):
            node = RedBlackBST.rotate_right(node)
        
        if not node.right:
            return None
        
        if (not RedBlackBST.is_red(node.right)) and (not RedBlackBST.is_red(node.right.left)):
            node = RedBlackBST.move_red_right(node)
        node.right = RedBlackBST.delete_max_node(node.right)
        return RedBlackBST.balance(node)

    @staticmethod
    def delete_min_node(node):
        if not node.left: return None
        if (not RedBlackBST.is_red(node.left)) and (not RedBlackBST.is_red(node.left.left)):
            node = RedBlackBST.move_red_left(node)
        node.left = RedBlackBST.delete_min_node(node.left)
        return RedBlackBST.balance(node)

    @staticmethod
    def move_red_right(node):
        RedBlackBST.flip_colors(node)
        if RedBlackBST.is_red(node.left.left):
            node = RedBlackBST.rotate_right(node)
            RedBlackBST.flip_colors(node)
        return node 
    
    @staticmethod
    def move_red_left(node):
        RedBlackBST.flip_colors(node)
        if RedBlackBST.is_red(node.right.left):
            node.right = RedBlackBST.rotate_right(node.right)
            node = RedBlackBST.rotate_left(node)
            RedBlackBST.flip_colors(node)
        return node 
    
    @staticmethod
    def put_node(node, key, value):
        if not node: return Node(key, value, True, 1)
        
        if key < node.key: node.left = RedBlackBST.put_node(node.left, key, value)
        elif key > node.key: node.right = RedBlackBST.put_node(node.right, key, value)
        else: node.value = value

        if RedBlackBST.is_red(node.right) and (not RedBlackBST.is_red(node.left)):  node = RedBlackBST.rotate_left(node)
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
        return node.color
    
    @staticmethod
    def flip_colors(node):
        node.color = not node.color 
        node.left.color = not node.left.color 
        node.right.color = not node.right.color 



if __name__ == '__main__':
    node = RedBlackBST()
    node.put('b', 'b')
    node.put('d', 'd')
    node.put('c', 'c')
    node.put('e', 'e')
    print(node.delete('e'))
    print(node.get('e'))
    