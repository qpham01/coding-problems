from collections import deque

class AdjacencyListGraph:
    def __init__(self, starts:list = None, ends:list = None):
        self.adjacencies = {}
        if starts is None or ends is None:
            return
        start_count = len(starts)
        end_count = len(ends)
        if (start_count != end_count): raise Exception("start count " + str(start_count) + " and end count " + str(end_count) + " must be equal")
        for i in range(start_count):
            start = starts[i]
            if start not in self.adjacencies:
                self.adjacencies[start] = []
            self.adjacencies[start].append(ends[i])
            
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
        for neighbor in neighbors:
            if neighbor not in to_visit:
                to_visit.add(neighbor)
                queue.append(neighbor)
        self.bfs_visit(queue, visits, to_visit, target)
        
    def dfs(self, start, target = None):
        if start not in self.adjacencies: raise Exception("Cannot find start node " + str(start))
        visits = []
        visited = set()
        target = self.dfs_visit(start, visits, visited, target)
        return [target, visits]
        
    def dfs_visit(self, node, visits:list, visited:set, target):
        visits.append(node)
        visited.add(node)
        if node == target: return target
        neighbors = self.adjacencies.get(node)
        if neighbors is None: return
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dfs_visit(neighbor, visits, visited, target)