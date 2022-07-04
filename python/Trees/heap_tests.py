from collections import deque
from heap import Heap

inputs = deque([50, 40, 25, 20, 35, 10, 15])
heap1 = Heap(inputs, True)
assert inputs == heap1.dataList
heap1.insert(45)
print("insert 45", heap1.dataList)
assert heap1.dataList[1] == 45
assert heap1.dataList[len(heap1.dataList) - 1] == 20
heap1.insert(75)
print("insert 75", heap1.dataList)
assert heap1.dataList[0] == 75
assert heap1.dataList[1] == 50
assert heap1.dataList[2] == 25
assert heap1.dataList[3] == 45
assert heap1.dataList[len(heap1.dataList) - 1] == 40
max_value = heap1.pop()
assert max_value == 75
print("pop 75", heap1.dataList)
assert heap1.dataList[0] == 50
assert heap1.dataList[1] == 45
assert heap1.dataList[2] == 25
assert heap1.dataList[3] == 40

heap2 = Heap(inputs, False)
print(heap2.dataList)
assert heap2.dataList == deque([10, 25, 15, 50, 35, 40, 20])
heap2.insert(12)
print("insert 12", heap2.dataList)
assert heap2.dataList[0] == 10
assert heap2.dataList[1] == 12
min_value = heap2.pop()
assert min_value == 10
print("pop 10", heap2.dataList)
assert heap2.dataList[0] == 12
assert heap2.dataList[1] == 25
