


class Node:

    data = None
    next = None
    visited = None

    def __init__(self, value):
        self.data = value


class LinkedList:

    head = None
    last = None

    size = 0

    def __init__(self, arr=[]):

        for i in arr:
            self.add(i)

    def __str__(self):

        return '->'.join([node.data for node in self.listToArray()]) + '->Nil'

    def listToArray(self):

        result = []
        node = self.head
        while node:
            result.append(node)
            node = node.next
        return result

    def add(self, value):

        node = self.head
        if not node:
            self.head = Node(value)
            return
        while node.next:
            node = node.next
        node.next = Node(value)
        self.size += 1

    def isPalindrome(self):
        """
        finds whether linked list is a palindrom or not
        :return:
        """
        _stk = []
        node = self.head
        while node:
            _stk.append(node.data)
            node = node.next
        node = self.head
        while node:
            if node.data != _stk.pop():
                return False
            node = node.next
        return not _stk

    def isPalindromeRecursive(self):
        """
        finds whether linked list is a palindrom or not,recursively
        :return:
        """
        """"
        def in_func(node, n):
            if node is None or n <= 0:
                return True
            i = 0
            temp_node = node
            lhs = node.data
            while i < n-1:
                i += 1
                temp_node = temp_node.next
            if lhs == temp_node.data:
                return True and in_func(node.next, n-2)
            else:
                return False and in_func(node.next, n-2)

        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return in_func(self.head, length)"""
        left = None

        def in_func(right):

            global left
            left = self.head
            if right is None:
                return True
            flag1 = in_func(right.next)
            if not flag1:
                return False
            flag2 = right.data == left.data
            left = left.next
            return flag2

        return in_func(self.head)

    def reverse(self):

        node = self.head
        prev = None
        _next = None
        while node:
            _next = node.next
            node.next = prev
            prev = node
            node = _next
        self.head = prev

    def reverseRecursive(self):

        def inner(_node):
            if _node is None:
                return
            inner(_node.next)
            print(_node.data,end='->')

        return inner(self.head)







    def traverse(self, node):

        """
        recursive traversal
        :param node:
        :return:
        """

        if not node:
            print('Nil')
            return
        print(node.data, end='->')
        self.traverse(node.next)

