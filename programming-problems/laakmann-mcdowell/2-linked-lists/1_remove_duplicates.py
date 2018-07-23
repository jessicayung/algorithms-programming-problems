"""
2.1 Remove Duplicates

Write code to remove duplicates from an unsorted linked list.

How would you solve this problem if a temporary buffer is not allowed?

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


def remove_duplicates(first_node):
    """
    :type first_node: LinkedListNode
    """

    set_of_values = set()
    previous_node = None
    current_node = first_node
    while current_node is not None:
        # If duplicate
        if current_node.value in set_of_values:
            # Remove node
            previous_node.next = current_node.next
        else:
            # If not duplicate, add value to set of values
            set_of_values.add(current_node.value)
            previous_node = current_node
        # Move to next node: update previous and current nodes
        current_node = current_node.next


def remove_duplicates_no_temp_buffer(first_node):
    current_node = first_node
    while current_node is not None:
        runner_node = current_node
        while runner_node is not None:
            if runner_node.next.value == current_node.value:
                runner_node.next = runner_node.next.next
            else:
                runner_node = runner_node.next
        current_node = current_node.next


class Test(unittest.TestCase):
    """Test"""

    def set_up_linked_list(self):
        a = LinkedListNode(1)
        b = LinkedListNode(2)
        c = LinkedListNode(3)
        d = LinkedListNode(2)
        e = LinkedListNode(4)
        f = LinkedListNode(3)
        g = LinkedListNode(5)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        f.next = g
        return a

    def test_remove_duplicates(self):
        a = self.set_up_linked_list()
        remove_duplicates(a)
        self.assertEqual(a, a)
        self.assertEqual(a.next.value, 2)
        self.assertEqual(a.next.next.next.value, 4)

    def test_remove_duplicates_no_buffer(self):
        a = self.set_up_linked_list()
        remove_duplicates(a)
        self.assertEqual(a, a)
        self.assertEqual(a.next.value, 2)
        self.assertEqual(a.next.next.next.value, 4)

if __name__ == '__main__':
    unittest.main()
