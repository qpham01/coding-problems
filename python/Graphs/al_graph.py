from collections import deque
from dis import dis
from math import dist

class AdjacencyListGraph:
    def __init__(self, starts:list = None, ends:list = None, weights:list = None):
        self.adjacencies = {}
        self.weights = {}
        if starts is None or ends is None:
            return
        start_count = len(starts)
        end_count = len(ends)
        if (start_count != end_count): raise Exception("start count " + str(start_count) + " and end count " + str(end_count) + " must be equal")
        if weights is None:
            weights = []
            for i in range(start_count):
                weights.append(1)
        for i in range(start_count):
            start = starts[i]
            if start not in self.adjacencies:
                self.adjacencies[start] = []
                self.weights[start] = []
            self.adjacencies[start].append(ends[i])
            self.weights[start].append(weights[i])

    def bfs(self, start, target = None):
        if start not in self.adjacencies: raise Exception("Cannot find start node " + str(start))
        queue = deque()
        queue.append(start)
        visits = []
        to_visit = {start}
        target = self.bfs_visit(queue, visits, to_visit, target)
        return [target, visits]
        
    def bfs_visit(self, queue:deque, visits:list, to_visit:set, target):
        if len(queue) == 0: return None
        node = queue.popleft()
        visits.append(node)
        if node == target: return target
        neighbors = self.adjacencies.get(node)
        if neighbors is None: return
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor not in to_visit:
                to_visit.add(neighbor)
                queue.append(neighbor)
        self.bfs_visit(queue, visits, to_visit, target)
        
    def dfs(self, start, target = None):
        if start not in self.adjacencies: raise Exception("Cannot find start node " + str(start))
        visits = []
        visited = set()
        distances = []
        target = self.dfs_visit(start, visits, distances, visited, 0, target)
        return [target, visits, distances]
        
    def dfs_visit(self, node, visits:list, distances:list, visited:set, distance:int, target):
        visits.append(node)
        visited.add(node)
        distances.append(distance)
        if node == target: return target
        neighbors = self.adjacencies.get(node)
        weights = self.weights.get(node)
        if neighbors is None: return
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor not in visited:
                self.dfs_visit(neighbor, visits, distances, visited, distance + weights[i], target)