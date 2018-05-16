from trees import *


succ = None
prev = None
f, m, l = None, None, None


def is_bst(root):

    # inefficient and poor
    if root is None:
        return True
    res = is_bst(root.left) and is_bst(root.right)
    if root.left:
        if root.left.data < root.data:
            res = res and True
        else:
            res = res and False
    if root.right:
        if root.right.data > root.data:
            res = res and True
        else:
            res = res and False
    return res


def is_bst2(root):

    global prev
    if root is None:
        return True
    if not is_bst2(root.left):
        return False
    if prev and prev.data > root.data:
        return False
    prev = root
    return is_bst2(root.right)
    # return True


def bst_min(root):

    if root is None or root.left is None:
        return root
    return bst_min(root.left)


def bst_search(root, key):

    if root is None:
        return root
    elif root.data == key:
        return root
    elif root.data > key:
        return bst_search(root.left, key)
    elif root.data < key:
        return bst_search(root.right, key)


def lowest_common_ancestors(root, key1, key2):

    if root is None:
        return
    elif root.data > key1 and root.data > key2:
        lowest_common_ancestors(root.left, key1, key2)
    elif root.data < key1 and root.data < key2:
        lowest_common_ancestors(root.right, key1, key2)
    else:
        return root.data


def inorder_successor(root, key):

    def _recurr(in_root, in_key):

        global succ
        if in_root is None:
            return None
        if in_root.data > in_key:
            succ = in_root
            _recurr(in_root.left, in_key)

        elif in_root.data < in_key:
            _recurr(in_root.right, in_key)
        return succ.data

    node = bst_search(root, key)
    if root is None:
        return root
    if node.right:
        return bst_min(root.right).data
    else:
        return _recurr(root, key)


def ksmallest(root, k, res=None):

    if res is None:
        res = []
    if root is None or len(res) == k:
        return res and res[-1]
    ksmallest(root.left, k, res)
    if len(res) != k:
        res.append(root)
    return ksmallest(root.right, k, res)


def bst_correction(root):

    def correction_util(in_root):

        global prev, f, m, l
        if in_root is None:
            return
        correction_util(in_root.left)
        if prev and prev.data > in_root.data:
            if f is None:
                f = prev
                m = in_root
            else:
                l = in_root
        prev = in_root
        return correction_util(in_root.right)

    correction_util(root)
    if f and l:
        temp = f.data
        f.data = l.data
        l.data = temp
    elif f and m:
        temp = f.data
        f.data = m.data
        m.data = temp
    return root
