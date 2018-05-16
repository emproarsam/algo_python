from trees.bst import *


if __name__ == "__main__":
    input_seq1 = [30, 45, 40, 50, 60, 55, 70]
    tree1 = growTree(input_seq1)
    tree2 = Node(30)
    # input_seq2 = [30, 40, 45]
    # subtree1 = growTree(input_seq2)
    # print("LCA for given tree = > are:\n{}".format(lowest_common_ancestors(tree1, 30, 70)))
    # print("Do tree1 has {:d}?\n{:d}".format(60, bst_search(tree1, 60).data))
    # print("min value node in tree1 is: {}".format(bst_min(tree1).data))
    # print(inorder_successor(tree1, 30))
    # print("The given tree => tree1 is a BST.\n{}".format(is_bstII(tree1)))
    # for i in range(1,8):
    #     print(ksmallest(tree1, i).data)
    # print(ksmallest(tree1, 2))
    print(bst_correction(tree2))
