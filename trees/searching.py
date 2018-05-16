from trees import growTree, height, nodesAtALevel


def bfs(root):
    node = root
    h = height(node)
    for level in range(h+1):
        nodesAtALevel(node, level)
        print(end='\n')


if __name__ == "__main__":
    input_seq = [30, 45, 40, 50, 60, 55, 70]
    tree1 = growTree(input_seq)
    bfs(tree1)

