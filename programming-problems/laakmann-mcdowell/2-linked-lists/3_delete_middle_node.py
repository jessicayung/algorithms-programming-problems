"""
2.3 Delete Middle Node

Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node.

EXAMPLE:
Input: node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f

"""

"""
Thoughts: need to change b.next even though we don't have access to b.
This is a singly linked list so cannot say c.prev.next = c.next etc.
"""
from linked_list_classes import LinkedListNode
import unittest

def solution(input_node):
    # How do we check that the input node is not the first node?
    if input_node.next is not None:
        next_node = input_node.next
        input_node.value = next_node.value
        input_node.next = next_node.next
    return input_node


class Tests(unittest.TestCase):

    def test_solution(self):
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
        solution(e)
        self.assertEqual(d.next.value, 6)
        self.assertEqual(d.next.next, g)
        self.assertEqual(f.next, g)

if __name__ == '__main__':
    unittest.main()
