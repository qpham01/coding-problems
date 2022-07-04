from collections import deque
from math import floor

class Heap:
    def __init__(self, data:list = None, max_heap:bool = False):
        self.max_heap = max_heap
        self.dataList = deque()
        if data is None: return
        for value in data:
            self.insert(value)

    def left_child_index(self, parent_index:int):
        return 2 * parent_index + 1
    
    def right_child_index(self, parent_index:int):
        return 2 * parent_index + 2
    
    def parent_index(self, child_index:int):
        return floor((child_index - 1) / 2)
    
    def get_parent_value(self, index:int):
        pindex = self.parent_index(index)
        return self.dataList[pindex]
    
    def swap_values(self, index1:int, index2:int):
        temp = self.dataList[index1]
        self.dataList[index1] = self.dataList[index2]
        self.dataList[index2] = temp
        
    def rotate_up_max(self, index:int, value):
        parent_value = self.get_parent_value(index)
        while value > parent_value:
            parent_index = self.parent_index(index)
            self.swap_values(index, parent_index)
            index = parent_index
            if index == 0: break
            parent_value = self.get_parent_value(index)            

    def rotate_up_min(self, index:int, value):
        parent_value = self.get_parent_value(index)
        while value < parent_value:
            parent_index = self.parent_index(index)
            self.swap_values(index, parent_index)
            index = parent_index
            if index == 0: break
            parent_value = self.get_parent_value(index)

    def rotate_down_max(self, index:int, value):
        l = len(self.dataList)
        if index >= l - 1: return
        right_index = self.right_child_index(index)
        left_index = self.left_child_index(index)
        if left_index >= l: return
        left_value = self.dataList[left_index]
        if right_index >= l:
            if value > left_value: return
            else: 
                self.swap_values(index, left_index)
        else:
            right_value = self.dataList[right_index]
            if value > right_value and value > left_value: return
            if left_value > right_value:
                self.swap_values(index, left_index)
                self.rotate_down_max(left_index, value)
            else:
                self.swap_values(index, right_index)
                self.rotate_down_max(right_index, value)
                        
    def rotate_down_min(self, index:int, value):
        l = len(self.dataList)
        if index >= l - 1: return
        right_index = self.right_child_index(index)
        left_index = self.left_child_index(index)
        if left_index >= l: return
        left_value = self.dataList[left_index]
        if right_index >= l:
            if value < left_value: return
            else: 
                self.swap_values(index, left_index)
        else:
            right_value = self.dataList[right_index]
            if value < right_value and value < left_value: return
            if left_value < right_value:
                self.swap_values(index, left_index)
                self.rotate_down_min(left_index, value)
            else:
                self.swap_values(index, right_index)
                self.rotate_down_min(right_index, value)
             
    def rotate_up_min(self, index:int, value):
        parent_value = self.get_parent_value(index)
        while value < parent_value:
            parent_index = self.parent_index(index)
            self.swap_values(index, parent_index)
            index = parent_index
            if index == 0: break
            parent_value = self.get_parent_value(index)
            
    def insert(self, value):
        self.dataList.append(value)
        index = len(self.dataList) - 1
        if (self.max_heap): self.rotate_up_max(index, value)
        else: self.rotate_up_min(index, value)
        
    def pop(self):
        pop_value = self.dataList.popleft()
        end_value = self.dataList.pop()
        self.dataList.appendleft(end_value)
        if (self.max_heap):
            self.rotate_down_max(0, end_value)
        else:
            self.rotate_down_min(0, end_value)
        return pop_value