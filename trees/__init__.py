DIAMETER_PARAMS = {
                    'nodes' : 3,
                    'edges' : 2
                  }


def swap(seq, i, j):
    """
    Swap 2 positions in a list
    :param seq:
    :param i:
    :param j:
    :return:
    """
    _temp = seq[i]
    seq[i] = seq[j]
    seq[j] = _temp


class Node:
    """
    An instance of a Tree's node
    """
    def __init__(self, _data):
        self.data = _data
        self.left = None
        self.right = None
        self.parent = None
        self.sibling = None
        self.rightThread = None
        self.balance = 0

    def __str__(self):

        return "Value of the node is {:d}".format(self.data)

    def __repr__(self):

        return "Value of the node is {:d}".format(self.data)


def __assignNode(nodeData, pNode):
    """
    Assigns nodes to their respective place in a tree
    :param nodeData:
    :param pNode:
    :return:
    """

    lNode = Node(nodeData)
    if lNode.data < pNode.data:
        if pNode.parent and (not pNode.parent.left) and (lNode.data < pNode.parent.data):
            pNode.parent.left = lNode
        else:
            pNode.left = lNode
            lNode.parent = pNode
        pNode = lNode
    else:
        if pNode.parent and (not pNode.parent.right) and (lNode.data > pNode.parent.data):
            pNode.parent.right = lNode
        else:
            pNode.right = lNode
            lNode.parent = pNode
        pNode = lNode
    return pNode


def growTree(seq):
    """
    Convert a given list into a Tree
    :param seq:
    :return:
    """

    if not seq:
        raise Exception('Empty list passed!!!!')
    rootIndex = int(len(seq)/2)
    root = Node(seq[rootIndex])
    if rootIndex == 0:
        return root
    node = root
    for i in range(rootIndex-1, -1, -1):
        node = __assignNode(seq[i], node)
    node = root
    for i in range(rootIndex+1, len(seq)):
        node = __assignNode(seq[i], node)
    return root


def height(root):
    """
    Height of a Tree
    :param root:
    :return:
    """
    node = root
    if root is None:
        return -1
    # lLen = height(node.left)
    # rLen = height(node.right)
    # if lLen > rLen:
    #     return lLen + 1
    # else:
    #     return rLen + 1
    return 1 + max([height(node.left), height(node.right)])


def nodesAtALevel(root, level, result=None):
    """
    Gives nodes a level of a Tree
    :param root:
    :param level:
    :return:
    """
    if result is None:
        result = []
    node = root
    if node is None:
        return []
    if level == 0:
        # print(node.data, end=',')
        # return node
        result.append(node)
    nodesAtALevel(node.left, level-1, result)
    nodesAtALevel(node.right, level-1, result)
    # return lNodes + rNodes
    return result


def inorderTraversal(root):
    """
    Inorder traversal : left child -> parent -> right child
    :param root:
    :return:
    """
    node = root
    if root is None:
        return
    inorderTraversal(node.left)
    print(node.data),
    inorderTraversal(node.right)


def diameter(root, parameter = DIAMETER_PARAMS['edges']):
    """
    Diameter of a Tree
    :param root:
    :param parameter:
    :return:
    """
    node = root
    if node is None:
        return 0
    d1 = diameter(node.left, parameter)
    d2 = diameter(node.right, parameter)
    rootHeights = height(node.left) + height(node.right) + parameter
    return max([d1, d2, rootHeights])


def ancestors(root, x):

    node = root
    if node is None:
        return False
    # if (node.left and node.left.data == x) or (node.right and node.right.data == x):
    if node.data == x:
        return True
    flag1 = ancestors(node.left, x)
    flag2 = ancestors(node.right, x)
    if flag1 or flag2:
        print(node.data)
    return flag1 or flag2


def width(root, result=0):

    node = root

    if node is None:
        return 0
    for level in range(height(node) + 1):
        result = max([result, len(nodesAtALevel(node,level))])
    return result


def  widthII(root):

    node = root
    if node is None:
        return
    _Q = [node]
    width = 0
    while _Q:
        _size = len(_Q)
        _width = max([width, _size])
        while _size:
            _temp = _Q.pop(0)
            if _temp.left:
                _Q.append(_temp.left)
            if _temp.right:
                _Q.append(_temp.right)
            _size -= 1
    return _width


def widthIII(root):

    def _widthRecur(tNode, _arr, level):

        if tNode:
            _arr[level] = _arr[level] + 1
            _widthRecur(tNode.left, _arr, level+1)
            _widthRecur(tNode.right, _arr, level+1)

    node = root
    if node is None:
        return
    _temp = [0 for i in range(10)]
    _widthRecur(node, _temp, 0)
    return max(_temp)


def isSubTree(tree, subTree):

    def _recur(tTree, tSubTree):
        if tSubTree is None:
            return True
        if tTree.data != tSubTree.data:
            return False
        return _recur(tTree.left, tSubTree.left) and _recur(tTree.right, tSubTree.right)

    if tree is None:
        return False
    if subTree is None:
        return True
    if tree.data == subTree.data:
        return _recur(tree, subTree)
    return isSubTree(tree.left, subTree) or isSubTree(tree.right, subTree)
