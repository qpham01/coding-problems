from tkinter.messagebox import NO
from binary_tree import BinaryTree, BinaryNode

class BinarySearchTree(BinaryTree):
    def __init__(self, data:list = None):
        self.root = None
        if data is not None:
            for value in data:
                if isinstance(value, list):
                    self.insert_node(value)
                else:
                    self.insert_ordered_node(None, value)
                    
    def insert_ordered_node(self, parent, value):
        if self.root is None:
            self.root = BinaryNode(value)
            return
        if parent is None: 
            parent = self.root
        if value < parent.data:
            if parent.left is None:
                parent.left = BinaryNode(value)
            else:
                self.insert_ordered_node(parent.left, value)
        else:
            if parent.right is None:
                parent.right = BinaryNode(value)
            else:
                self.insert_ordered_node(parent.right, value)