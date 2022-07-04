class AdjacencyMatrixGraph:
    def __init__(self, node_count:int = 0, adjacencies:dict = None):
        self.node_values = []
        self.adjacencies = []
        for i in range(node_count):
            self.node_values.append(i)
        for i in range(node_count):
            self.adjacencies.append([])
            for j in range(node_count):
                self.adjacencies[i].append(0)