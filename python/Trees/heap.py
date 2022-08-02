from collections import deque
from math import floor
from turtle import right

class Heap:
    def __init__(self, max_heap:bool = False, data:list = None):
        self.queue = deque()
        self.max_heap = max_heap
        if data is None: return
        for value in data:
            self.insert(value)
    
    def __len__(self):
        return len(self.queue)
    
    def left_child_index(self, parent_index:int):
        return 2 * parent_index + 1
    
    def right_child_index(self, parent_index:int):
        return 2 * parent_index + 2
    
    def parent_index(self, child_index:int):
        return floor((child_index - 1) / 2)
    
    def get_parent_value(self, index:int):
        pindex = self.parent_index(index)
        return self.queue[pindex]
    
    def swap_values(self, index1:int, index2:int):
        temp = self.queue[index1]
        self.queue[index1] = self.queue[index2]
        self.queue[index2] = temp
    
    def is_max(self):
        return self.max_heap
    
    def should_rotate_up(self, parent, value):
        if self.max_heap:
            return value > parent
        else:
            return value < parent

    def should_rotate_down(self, child, value):
        if self.max_heap:
            return value < child
        else:
            return value > child
        
    def rotate_up(self, index:int, value):
        if index == 0: return
        parent_index = self.parent_index(index)
        parent = self.queue[parent_index]
        if self.should_rotate_up(parent, value):
            self.swap_values(parent_index, index)
            self.rotate_up(parent_index, value)
            
    def rotate_down(self, index:int, value):
        l = len(self.queue)
        if index >= l: return
        left_child_index = self.left_child_index(index)
        if left_child_index >= l: return
        left_child_value = self.queue[left_child_index]
        right_child_index = self.right_child_index(index)
        if right_child_index >= l:
            if self.should_rotate_down(left_child_value, value):
                self.swap_values(right_child_index, index)
            return
        right_child_value = self.queue[right_child_index]
        should_rotate_left = (self.max_heap and left_child_value > right_child_value) or (not self.max_heap and left_child_value < right_child_value)
        if should_rotate_left:
            self.swap_values(left_child_index, index)
            self.rotate_down(left_child_index, value)
        should_rotate_right = (self.max_heap and left_child_value < right_child_value) or (not self.max_heap and left_child_value > right_child_value)    
        if should_rotate_right:
            self.swap_values(right_child_index, index)
            self.rotate_down(right_child_index, value)
                        
    def insert(self, value):
        self.queue.append(value)
        index = len(self.queue) - 1
        self.rotate_up(index, value)
        
    def pop(self):
        pop_value = self.queue.popleft()
        end_value = self.queue.pop()
        self.queue.appendleft(end_value)
        self.rotate_down(0, end_value)
        return pop_value