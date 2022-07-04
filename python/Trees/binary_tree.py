class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def __init__(self, data:list):
        self.root = None
        for item in data:
            self.insert_node(item[0], item[1], item[2])
            
    def insert_node(self, data, parent, left:bool):
        if parent is None:
            if self.root is None: self.root = BinaryNode(data)
            else: raise Exception("parent not found")
        else:
            [_, parent_node, _] = self.dfs_preorder(parent)
            if parent_node is None: 
                message = "parent " + str(parent) + " not found"
                raise Exception(message)
            if left:
                if parent_node.left is None: parent_node.left = BinaryNode(data)
                else: raise Exception("left node of", parent, "already occupied")
            else:
                if parent_node.right is None: parent_node.right = BinaryNode(data)
                else: raise Exception("right node of", parent, "already occupied")
                        
    def dfs_preorder(self, target):
        if self.root is None: return None
        visited = []
        result = self.preorder_search(visited, self.root, 1, target)
        result.append(visited)
        return result
        
    def preorder_search(self, visited:list, node:BinaryNode, height:int, target):
        if node is None: 
            return [height, None]
        visited.append(node.data)
        if node.data == target:
            return [height, node]
        leftHeight = height
        rightHeight = height
        if node.left is not None:
            leftResult = self.preorder_search(visited, node.left, height + 1, target)
            if leftResult is not None:
                leftHeight = leftResult[0]
                if leftResult[1] is not None:
                    return leftResult
        if node.right is not None:
            rightResult = self.preorder_search(visited, node.right, height + 1, target)
            if rightResult is not None:
                rightHeight = rightResult[0]        
                if rightResult[1] is not None:
                    return rightResult
        height = max(leftHeight, rightHeight)
        return [height, None]
        
    def height(self):
        [height, _, _] = self.dfs_preorder(float('inf'))
        return height