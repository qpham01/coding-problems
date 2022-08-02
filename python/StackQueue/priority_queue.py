from sys import path
path.append("..")
from Trees.heap import Heap

class PriorityQueue:
    def __init__(self, max_heap:bool = False):
        self.heap = Heap(None, max_heap)
    
    def __len__(self):
        return len(self.heap)
        
    def push(self, value):
        self.heap.insert(value)
        
    def pop(self):
        if len(self.heap) == 0: raise Exception("Queue is empty")
        return self.heap.pop()
