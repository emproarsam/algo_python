from trees import growTree, height, diameter, ancestors, nodesAtALevel, width, widthII, widthIII, isSubTree


def ancestors(root, x):

    seq = []

    def _recur(root, x, res):

        if root is None:
            return False
        if root.data == x:
            return True
        _temp = root
        if _recur(_temp.left, x, res) or _recur(_temp.right, x, res):
            res.append(root.data)
            return True
        return False

    _recur(root, x, seq)
    return seq


if __name__ == "__main__":
    input_seq1 = [30, 45, 40, 50, 60, 55, 70]
    tree1 = growTree(input_seq1)
    input_seq2 = [30, 40, 4]
    subtree1 = growTree(input_seq2)
    # print("Height of the given tree => tree1 is {}".format(height(tree1)))
    # print("Diameter of the given tree => tree1 is {}".format(diameter(tree1)))
    # print("Ancestors of {} in tree1 are {}".format(55, ancestors(tree1, 55)))
    # print("No. of nodes at level {}, for the given tree => tree1 are {}".format(2, [i.data for i in nodesAtALevel(tree1, 2)]))
    # print("The width of the tree => tree1 is {}".format(width(tree1)))
    # print("The width of the tree => tree1 is {}".format(widthII(tree1)))
    # print("The width of the tree => tree1 is {}".format(widthIII(tree1)))
    # print("The ancestors of the node => {}".format(ancestors(tree1, 30)))
    print("subtree1 is a subtree of tree1 : {}".format(isSubTree(tree1, subtree1)))