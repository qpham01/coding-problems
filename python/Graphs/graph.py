
from collections import deque
class NonDirectedGraph:
    def __init__(self, starts: list, ends:list, weights:list):
        self.adjacencies = {}
        self.weights = {}
        if starts is None or ends is None: return
        
        start_counts = len(starts)
        end_counts = len(ends)
        weight_count = len(weights)
        if (start_counts != end_counts or start_counts !=end_counts): raise Exception("invalid inputs")
        for i in range(start_counts):
            start = starts[i]
            if start not in self.adjacencies:
                self.adjacencies[start] = []
                self.weights[start] = []
            self.adjacencies[start].append(ends[i])
            self.weights[start].append(weights[i])
            end = ends[i]
            if end not in self.adjacencies:
                self.adjacencies[end] = []
                self.weights[end] = []
            self.adjacencies[end].append(starts[i])
            self.weights[end].append(weights[i])
            
    def get_node_count(self):
        return len(self.adjacencies)
    
    def get_edge_count(self):
        edge_count = 0
        for n in self.adjacencies:
            edge_count += len(self.adjacencies[n])
        return edge_count
    
    def bfs(self, start, target = None):
        if start not in self.adjacencies: raise Exception("Node " + str(start) + " not found")
        queue = deque()
        queue.append(start)
        visited = []
        to_visit = {start}
        found = self.bfs_visit(queue, visited, to_visit, target)
        return [found, visited]
        
    def bfs_visit(self, queue:deque, visited:list, to_visit:set, target):
        if len(queue) == 0: return None
        n = queue.popleft()
        visited.append(n)
        if n == target: return n
        next = self.adjacencies.get(n)
        if next is None: return None
        for nn in next:
            if nn in to_visit: continue
            to_visit.add(nn)
            queue.append(nn)
        return self.bfs_visit(queue, visited, to_visit, target)
            
# Tests
        
graph = NonDirectedGraph([1, 2, 3, 3], [2, 3, 1, 4], [1, 1, 1, 1])
print(graph.adjacencies)
assert graph.get_edge_count() == 8
assert graph.get_node_count() == 4
[found, visited] = graph.bfs(1, 4)
print(found)
print(visited)
assert len(visited) == 4
assert found == 4
