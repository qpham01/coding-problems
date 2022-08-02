from collections import deque
from heap import Heap

inputs = deque([50, 40, 25, 20, 35, 10, 15])
heap1 = Heap(True, inputs)
assert inputs == heap1.queue
heap1.insert(45)
print("insert 45", heap1.queue)
assert heap1.queue[1] == 45
assert heap1.queue[len(heap1.queue) - 1] == 20
heap1.insert(75)
print("insert 75", heap1.queue)
assert heap1.queue[0] == 75
assert heap1.queue[1] == 50
assert heap1.queue[2] == 25
assert heap1.queue[3] == 45
assert heap1.queue[len(heap1.queue) - 1] == 40
max_value = heap1.pop()
assert max_value == 75
print("pop 75", heap1.queue)
assert heap1.queue[0] == 50
assert heap1.queue[1] == 45
assert heap1.queue[2] == 25
assert heap1.queue[3] == 40

print("Pre pop 50", heap1.queue)
max_value = heap1.pop()
assert max_value == 50
print("pop 50", heap1.queue)
assert heap1.queue[0] == 45
assert heap1.queue[1] == 40
assert heap1.queue[2] == 25
assert heap1.queue[3] == 20
assert heap1.queue[4] == 35
assert heap1.queue[5] == 10
assert heap1.queue[6] == 15

heap2 = Heap(False, inputs)
print(heap2.queue)
assert heap2.queue == deque([10, 25, 15, 50, 35, 40, 20])
heap2.insert(12)
print("insert 12", heap2.queue)
assert heap2.queue[0] == 10
assert heap2.queue[1] == 12
min_value = heap2.pop()
assert min_value == 10
print("pop 10", heap2.queue)
assert heap2.queue[0] == 12
assert heap2.queue[1] == 25
