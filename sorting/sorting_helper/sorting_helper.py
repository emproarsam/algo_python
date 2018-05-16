from sorting import random_list_generator

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root):
        self.root = root

    def traversal(self,node=None):
        _node = node
        if _node and (_node.right or _node.left):
            self.traversal(_node.left)
            self.traversal(_node.right)
        print(_node.data)


if __name__=="__main__":
    t = Tree(Node(50))
    t_root = t.root
    t_root.left = Node(40)
    t_root.right = Node(60)
    t_root.left.left = Node(20)
    t_root.left.right = Node(30)
    t_root.right.left = Node(70)
    t_root.right.right = Node(80)


    t.traversal(t_root)





