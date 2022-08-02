from priority_queue import PriorityQueue

pq = PriorityQueue()
pq.push(10)
pq.push(9)
pq.push(8)
pq.push(7)
pq.push(6)
pq.push(5)
pq.push(4)

assert pq.pop() == 4
assert pq.pop() == 5
assert pq.pop() == 6
assert pq.pop() == 7

pq.push(3)
pq.push(2)
pq.push(1)

assert pq.pop() == 1
assert pq.pop() == 2
assert pq.pop() == 3
assert pq.pop() == 8

pq = PriorityQueue(True)
pq.push(10)
pq.push(9)
pq.push(8)
pq.push(7)
pq.push(6)
pq.push(5)
pq.push(4)

assert pq.pop() == 10
assert pq.pop() == 9
assert pq.pop() == 8
assert pq.pop() == 7

pq.push(3)
pq.push(2)
pq.push(1)

assert pq.pop() == 6
assert pq.pop() == 5
assert pq.pop() == 4
assert pq.pop() == 3
