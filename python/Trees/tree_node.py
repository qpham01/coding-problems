class TreeNode:
    def __init__(self, data):
        self.data  = data
        self.children = {}
        
    def addChild(self, data):
        child = TreeNode(data)
        self.children[data] = child
        return child