from graphs import *


if __name__ == "__main__":

    g1 = GraphAL([[1], [], [0, 3]])
    g1.addEdge(3, 4)
    g1.addEdge(4, 2)
    print(g1)
    g1.dfs(2)
    # g1.detectCycle()
    g1.detectCycleDisJoinSet()
