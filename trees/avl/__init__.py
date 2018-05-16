from trees import *
from trees.bst import *


def avl_size(root):

    if root is None:
        return 0
    return avl_size(root.left) + 1 + avl_size(root.right)


def avl_height(root):

    if root is None:
        return -1
    return max([avl_height(root.left), avl_height(root.right)]) + 1


def avl_balancer(root):

    if root is None:
        return
    avl_balancer(root.left)
    root.balance = avl_height(root.right) - avl_height(root.left)
    avl_balancer(root.right)
    return root


def right_rotate(grandparent, parent):

    grandparent.left = parent.right
    parent.right = grandparent
    return parent


def left_rotate(grandparent, parent):

    grandparent.right = parent.left
    parent.left = grandparent
    return parent


def rotation(grandparent, parent):

    res = grandparent
    child = parent.left or parent.right
    if parent and parent is grandparent.left:
        if child and child is parent.right:
            grandparent.left = left_rotate(parent, child)
        res = right_rotate(grandparent, parent)

    elif parent and parent is grandparent.right:
        if child and child is parent.left:
            grandparent.right = right_rotate(parent, child)
        res = left_rotate(grandparent, parent)
    return res


def avl_insert(root, key):

    def bst_insert(in_root, in_key):

        if in_root is None:
            return Node(in_key)
        if in_root.data > in_key:
            in_root.left = bst_insert(in_root.left, in_key)
            in_root = avl_balancer(in_root)
            if in_root.balance <= -2 or in_root.balance >= 2:
                in_root = rotation(in_root, in_root.left)
        else:
            in_root.right = bst_insert(in_root.right, in_key)
            in_root = avl_balancer(in_root)
            if in_root.balance <= -2 or in_root.balance >= 2:
                in_root = rotation(in_root, in_root.right)
        in_root = avl_balancer(in_root)
        return in_root
    root = bst_insert(root, key)
    root = avl_balancer(root)

    return root
