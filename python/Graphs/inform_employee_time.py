# A company has n employees with unique ids from 0 to n-1. Head of company has id headID.
# Managers are represented by a manager array where managers[i] is id of the employee i.
# Each employee has one direct manager. The company head has no manager (managers[headID] = -1).
# The subordination hierarchy is guaranteed to be a tree.

# example inputs:
# - n = 8, so employee ids are [0..7]
# - headID = 4, so head of company has id 4
# - managers = [2, 2, 4, 6, -1, 4, 4, 5]

from al_graph import AdjacencyListGraph
class HierarchyTree(AdjacencyListGraph):
    def __init__(self, count:int, head_id:int, managers:list, inform_time:list):
        if managers is None or inform_time is None or count == 0 or head_id >= count or head_id < 0: raise Exception("Invalid data")
        if len(managers) != count or len(inform_time) != count: raise Exception("Invalid managers or inform time length")
        starts = []
        ends = []
        weights = []
        for i in range(count):
            starts.append(managers[i])
            ends.append(i)
            weights.append(inform_time[managers[i]])
        super().__init__(starts, ends, weights)