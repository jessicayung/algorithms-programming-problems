"""
6 Palindrome

Author: Jessica Yung
16 October 2016
"""
from linked_list_classes import LinkedListNode
import unittest

# If it's a doubly-linked list, it's easy. We just send a pointer to the end
# then have it trace back and compare the values one by one until ceiling(len/2).

def is_dll_palindrome(head):
    """`head` is a DoublyLinkedListNode."""
    current = head
    runner = head
    list_length = 1
    number_checked = 0
    # Send runner to the back
    while runner.next is not None:
        runner = runner.next
        list_length += 1
    while number_checked < int(list_length / 2 + 1):
        if current.value != runner.value:
            return False
        else:
            current = current.next
            runner = runner.prev
            number_checked += 1
    # All checked
    return True

# If it's a singly-linked list, then we go through it once and get the length.
# We may as well get all the values and put it in an array and compare?

def reverse_and_clone(node):
    prev = None
    while node is not None:
        current = LinkedListNode(node.value)
        current.next = prev
        prev = current
        node = node.next
    return prev


def is_equal_ll(head1, head2):
    node1 = head1
    node2 = head2
    while node1 is not None and node2 is not None:
        if node1.value != node2.value:
            print(node1.value, node2.value)
            return False
        node1 = node1.next
        node2 = node2.next
    return True


def is_sll_palindrome_reverse(head):
    reverse = reverse_and_clone(head)
    return is_equal_ll(head, reverse)

class Stack(object):
    def __init__(self, value):
        super(Stack, self).__init__()
        self.top = None

    def pop(self):
        """Removes and returns the top item"""
        removed = self.top
        self.top = self.top.next
        return removed

    def push(self, item):
        """Adds an item to the stack."""
        second = self.top
        self.top = LinkedListNode(item)
        self.top.next = second


def is_sll_palindrome_runners(head):
    slow = head
    fast = head
    faster = head
    if __name__ == '__main__':
        while faster is not None:
            fast = faster
            # TODO: Slow runner adds node values to a stack
            slow_stack.add(slow)
            # Shift nodes
            slow = slow.next
            faster = fast.next.next
        # If odd number of nodes
        if fast.next = None:
            # TODO: Drop first node from stack
        is_equal_ll(stacknode1, slow)



class Tests(unittest.TestCase):

    def test_sll_palindrome(self):
        a = LinkedListNode(9)
        b = LinkedListNode(7)
        c = LinkedListNode(6)
        d = LinkedListNode(5)
        e = LinkedListNode(6)
        f = LinkedListNode(7)
        g = LinkedListNode(9)
        # List 1: 679
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        f.next = g
        self.assertEqual(is_sll_palindrome_reverse(a), True)

if __name__ == '__main__':
    unittest.main()

"""
Mistakes:
- Initially wrote 'node1 != node2' instead of `node1.value != node2.value'.
"""