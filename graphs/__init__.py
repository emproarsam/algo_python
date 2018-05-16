from functools import reduce


class GraphAL():
    """
    Adjacency list representation of Graph
    """

    def __init__(self, _input=None):

        self.vertices = _input or []

    def __str__(self):

        res = []
        for vertex, adjList in enumerate(self.vertices):
            res.append('-->'.join([str(i) for i in [vertex] + adjList]))
        return '\n'.join(res)

    def __repr__(self):

        return self.__str__()

    def __addVertex(self):

        self.vertices.append([])

    def addEdge(self, u, v):

        if u < len(self.vertices) and v < len(self.vertices):
            self.vertices[u].append(v)
        else:
            self.__addVertex()
            self.addEdge(u, v)

    def dfs(self, s):

        _Stack = []
        _visited = []
        _Stack.append(s)
        _visited.append(s)
        while _Stack:
            currVertex = _Stack.pop()
            print(currVertex,end=' ')
            for vertex in self.vertices[currVertex]:
                if vertex not in _visited:
                    _Stack.append(vertex)
                    _visited.append(vertex)
        print()

    def detectCycle(self):

        def _innerDetectCycle(s):

            cycle = False
            _Stack = []
            _visited = []
            _Stack.append(s)
            _visited.append(s)
            while _Stack and not cycle:
                currVertex = _Stack.pop()
                for vertex in self.vertices[currVertex]:
                    if vertex not in _visited:
                        _Stack.append(vertex)
                        _visited.append(vertex)
                    else:
                        cycle = True
                        break
            return cycle

        for i in range(len(self.vertices)):
            if _innerDetectCycle(i):
                print("Given Graph contains a CYCLE")
                break

    def detectCycleDisJoinSet(self):

        parent = [-1 for vertex in range(len(self.vertices))]
        _cycle = False
        for u, adjList in enumerate(self.vertices):
            for v in adjList:
                _p = parent[v]
                while _p != -1 and _p != u:
                    _p = parent[_p]
                if _p == u:
                    _cycle = True
                    break
                parent[v] = u
            if _cycle:
                print("CYCLE FOUND!!!")
                break



