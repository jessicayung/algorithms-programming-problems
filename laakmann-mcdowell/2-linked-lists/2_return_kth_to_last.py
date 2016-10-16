"""
2.2 Return Kth to Last
Implement an algorithm to find the kth to last element of a singly linked list.

Author: Jessica Yung
15 October 2016
"""


import unittest


class LinkedListNode(object):
    """Singly Linked List Node"""

    def __init__(self, value):
        super(LinkedListNode, self).__init__()
        self.value = value
        self.next = None


def solution_one(head, k):
    current_node = head
    runner = current_node
    for i in range(k):
        if runner.next is not None:
            runner = runner.next
        else:
            print("No kth to last element.")
            return
    while runner.next is not None:
        runner = runner.next
        current_node = current_node.next
    return current_node


class Tests(unittest.TestCase):

    def set_up_linked_list(self):
        a = LinkedListNode(1)
        b = LinkedListNode(2)
        c = LinkedListNode(3)
        d = LinkedListNode(4)
        e = LinkedListNode(5)
        f = LinkedListNode(6)
        g = LinkedListNode(7)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        f.next = g
        return a


    def test_solution_one(self):
        a = self.set_up_linked_list()
        self.assertEqual(solution_one(a, 3).value, 4)
        self.assertEqual(solution_one(a, 0).value, 7)


if __name__ == '__main__':
    unittest.main()