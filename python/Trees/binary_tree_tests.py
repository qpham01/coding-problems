from binary_tree import BinaryTree

def test_list_init(input: list):
    tree = BinaryTree(input)
    return tree    

init_data = [[1, None, True], [2, 1, True], [3, 1, False]]
tree = test_list_init(init_data) 
assert tree.root.data == 1
assert tree.root.left.data == 2
assert tree.root.right.data == 3

init_data = [[1, None, True], [2, 1, True], [3, 1, False], [4, 2, True], [5, 4, False], [6, 5, False], [7, 3, False], [8, 7, True]]
tree = test_list_init(init_data) 
assert tree.root.data == 1
assert tree.root.left.data == 2
assert tree.root.right.data == 3
assert tree.root.left.left.data == 4
assert tree.root.left.right is None
assert tree.root.left.left.left is None
assert tree.root.left.left.right.data == 5
assert tree.root.left.left.left is None
assert tree.root.left.left.right.left is None
assert tree.root.left.left.right.right.data == 6
assert tree.root.right.left is None
assert tree.root.right.right.data == 7
assert tree.root.right.right.left.data == 8
assert tree.root.right.right.right is None

assert tree.height() == 5
targets = [0, 5, 3, 7, 8]
heights = [5, 4, 2, 3, 4]
for i in range(len(targets)):
    result = tree.dfs_preorder(targets[i])
    assert result[0] == heights[i]
    if result[1] is not None:
        assert result[1].data == targets[i]
    visited = result[2]
    print('search for ' + str(targets[i]) + ' visited', visited)
