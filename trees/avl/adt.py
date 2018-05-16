from trees.avl import *


if __name__ == "__main__":

    input_seq1 = [30, 45, 40, 50, 60, 55, 70]
    tree1 = growTree(input_seq1)
    # print("inorder traversal of tree1:{}".format(inorderTraversal(tree1)))
    # print("size of tree1:{}".format(avl_size(tree1)))
    # print("height of tree1:{}".format(avl_height(tree1)))
    # tree1.left = right_rotate(tree1.left, tree1.left.left)
    # tree1.right = left_rotate(tree1.right, tree1.right.right)
    avl_insert(tree1, 28)
    avl_insert(tree1, 26)
    # avl_balancer(tree1)
    # avl_insert(tree1, 68)
    print("inorder traversal of tree1:{}".format(inorderTraversal(tree1)))
