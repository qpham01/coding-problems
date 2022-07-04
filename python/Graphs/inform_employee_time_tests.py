from dis import dis
from inform_employee_time import HierarchyTree

count = 8
head_id = 4
tree1 = HierarchyTree(count, head_id, [2, 2, 4, 6, -1, 4, 4, 5], [0, 0, 4, 0, 7, 3, 6, 0])
[target, visits, distances] = tree1.dfs(head_id)
result = max(distances)
print(distances)
assert result == 13