from binary_search_tree import BinarySearchTree

tree1 = BinarySearchTree([12, 7, 5, 9, 18, 16, 25])
assert tree1.root.data == 12
assert tree1.root.left.data == 7
assert tree1.root.left.left.data == 5
assert tree1.root.left.right.data == 9
assert tree1.root.right.data == 18
assert tree1.root.right.left.data == 16
assert tree1.root.right.right.data == 25

