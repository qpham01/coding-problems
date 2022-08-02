# You are in charge of designing a small, in-memory social network, with the basic functionality of adding friendship
# between two people via an AddFriendship function, and a GetSuggestedFriends function for a particular user in the
# network. The criteria is to pick someone with whom the given user has the most number of friends in common.

# Approach: Graph, for person P, do a 1-level breadth-first search to get P's friends.
# For each friend F, do a 1-level breadth-first search top see if P is also a friend, if so add to common friend count fc for that F.
# Sort by the friend count fc for people to recommend as potential friends.

from collections import deque
from operator import ne

class FriendGraph:
    def __init__(self, starts:list = None, ends:list = None, weights:list = None):
        self.adjacencies = {}
        if starts is None or ends is None:
            return
        start_count = len(starts)
        end_count = len(ends)
        if (start_count != end_count): raise Exception("start count " + str(start_count) + " and end count " + str(end_count) + " must be equal")
        for i in range(start_count):
            start = starts[i]
            end = ends[i]
            self.addEdge(start, end, weights[i])
        
    def addEdge(self, start, end, weight:int):
            if start not in self.adjacencies:
                self.adjacencies[start] = {}
            self.adjacencies[start][end] = weight
            if end not in self.adjacencies:
                self.adjacencies[end] = {}
            self.adjacencies[end][start] = weight
           
    def addEdges(self, value, edges:list, weights:list):
        for i in range(len(edges)):
            weight = weights[i] if weights is list else 1
            self.addEdge(value, edges[i], weight)
        
    def bfs(self, start, max_depth:int, target = None):
        if start not in self.adjacencies: raise Exception("Cannot find start node " + str(start))
        queue = deque()
        queue.append(start)
        visits = []
        to_visit = {start}
        target = self.bfs_recurse(queue, 1, max_depth, visits, to_visit, target)
        return [target, visits]
    
    def bfs_recurse(self, queue:deque, depth:int, max_depth:int, visits:list, to_visit:set, target):
        while len(queue) > 0:
            node = queue.popleft()
            visits.append(node)
            if node == target: return node
            if depth < max_depth:
                for child_node in self.adjacencies.keys():
                    if child_node not in to_visit:
                        to_visit.add(child_node)
            return self.bfs_recurse(queue, depth + 1, max_depth, visits, to_visit, target) 
        return None

class Network:
    def __init__(self):
        self.Graph = FriendGraph([], [], [])        
        
    def AddPerson(self, person:str):
        self.Graph.addEdges(person, [], [])
    
    def AddFriend(self, person:str, friend:str):
        self.Graph.addEdge(person, friend, 1)
        
    def FriendCount(self, person:str):
        return len(self.Graph.adjacencies[person])

    def Friends(self, person:str):
        return self.Graph.adjacencies[person]
    
    def CommonFriends(self, person1:str, person2:str):
        common = set()
        friends1 = self.Friends(person1)
        friends2 = self.Friends(person2)
        for friend1 in friends1:
            for friend2 in friends2:
                if friend2 == friend1:
                    common.add(friend1)
        return common

network = Network()
network.AddFriend("Jane", "Mary")
network.AddFriend("Jane", "Moe")
network.AddFriend("Jane", "Manny")
network.AddFriend("Jane", "Paul")
network.AddFriend("Mary", "Paul")
network.AddFriend("Mary", "Peter")
network.AddFriend("Mary", "Payton")
network.AddFriend("Manny", "Paul")
network.AddFriend("Moe", "Peter")

assert network.FriendCount("Jane") == 4
assert network.FriendCount("Moe") == 2
assert network.FriendCount("Manny") == 2
assert network.FriendCount("Mary") == 4

janeMary = network.CommonFriends("Jane", "Mary")
print("Jane friends", network.Friends("Jane"))
print("Mary friends", network.Friends("Mary"))
print(janeMary)
assert len(janeMary) == 1
assert "Paul" in janeMary

maryMoe = network.CommonFriends("Mary", "Moe")
print(maryMoe)
assert len(maryMoe) == 2
assert "Jane" in maryMoe
assert "Peter" in maryMoe