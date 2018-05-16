

class Edge:

    def __init__(self, src=-1, dest=-1):

        self.src = src
        self.dest = dest


class GraphV2:

    def __init__(self, V, E):

        self.v = V
        self.e = E
        self.edge = [Edge() for i in range(self.e)]

    @staticmethod
    def find(parent, src):

        if parent[src] == -1:
            return src
        return GraphV2.find(parent, parent[src])

    @staticmethod
    def union(parent, x, y):

        xset = GraphV2.find(parent, x)
        yset = GraphV2.find(parent, y)
        parent[xset] = yset

    def isCycle(self):

        parent = [-1 for vertex in range(self.v)]
        _cycle = False

        for edge in self.edge:
            x = GraphV2.find(parent, edge.src)
            y = GraphV2.find(parent, edge.dest)
            if x == y:
                return True
            GraphV2.union(parent, x, y)
        return False

if __name__ == "__main__":

    g1 = GraphV2(5, 5)
    g1.edge[0].src = 0
    g1.edge[0].dest = 1
    g1.edge[1].src = 2
    g1.edge[1].dest = 0
    g1.edge[2].src = 2
    g1.edge[2].dest = 3
    g1.edge[3].src = 3
    g1.edge[3].dest = 4
    g1.edge[4].src = 4
    g1.edge[4].dest = 2
    if g1.isCycle():
        print("CYCLE is present!!!")
    else:
        print("CYCLE is not present!!!")
