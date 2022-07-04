from dis import dis
from al_graph import AdjacencyListGraph

graph0 = AdjacencyListGraph()
assert graph0.adjacencies == {}

starts1 = [0, 0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8]
ends1   = [1, 3, 0, 3, 8, 0, 2, 4, 5, 3, 6, 3, 4, 7, 6, 2]
graph1 = AdjacencyListGraph(starts1, ends1)
print(graph1.adjacencies)
[target, visits] = graph1.bfs(3)
assert target is None
print(visits)
assert visits == [3, 0, 2, 4, 5, 1, 8, 6, 7]
[target, visits, distances] = graph1.dfs(3)
assert target is None
print("visits", visits)
assert visits == [3, 0, 1, 2, 8, 4, 6, 7, 5]
print("distances", distances)
assert distances == [0, 1, 2, 1, 2, 1, 2, 3, 1]

starts2 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6]
ends2   = [2, 5, 1, 3, 5, 2, 4, 3, 5, 6, 1, 2, 4, 4]
graph2 = AdjacencyListGraph(starts2, ends2)
print(graph2.adjacencies)
[target, visits] = graph2.bfs(3)
assert target is None
print(visits)
assert visits == [3, 2, 4, 1, 5, 6]
[target, visits, distances] = graph2.dfs(3)
assert target is None
print("visits", visits)
assert visits == [3, 2, 1, 5, 4, 6]
print("distances", distances)
assert distances == [0, 1, 2, 3, 4, 5]