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
    while number_checked < int(list_length / 2 + 1)
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
        # Sum:
        h = sum_lists(a, d)
        print(h.value, h.next.value, h.next.next.value, h.next.next.next.value)

if __name__ == '__main__':
    unittest.main()