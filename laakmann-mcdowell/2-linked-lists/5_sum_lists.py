"""
2.5 Sum Lists

Author: Jessica Yung
16 October 2016
"""
from linked_list_classes import LinkedListNode
import unittest


def sum_lists(list_one_head, list_two_head):
    pointer_one = list_one_head
    pointer_two = list_two_head
    sum_list_start = 0
    carry = 0
    sum_head = None
    pointer_sum = None
    while pointer_one is not None or pointer_two is not None:
        if pointer_one is not None and pointer_two is not None:
            digit_sum = pointer_one.value + pointer_two.value + carry
        elif pointer_one is not None:
            digit_sum = pointer_one.value + carry
        else:
            digit_sum = pointer_two.value + carry
        print("Digit Sum: ", digit_sum)
        carry, new_digit = divmod(digit_sum, 10)
        print("Carry: ", carry, "New digit: ", new_digit)
        # Add resulting digit to 'sum' linked list and move pointer to that digit
        if sum_list_start == 0:
            sum_head = LinkedListNode(new_digit)
            pointer_sum = sum_head
            sum_list_start = 1
        else:
            pointer_sum.next = LinkedListNode(new_digit)
            pointer_sum = pointer_sum.next
        # Move to the next digit in the lists
        if pointer_one is not None:
            pointer_one = pointer_one.next
        if pointer_two is not None:
            pointer_two = pointer_two.next
    return sum_head


class Tests(unittest.TestCase):

    def test_partition(self):
        a = LinkedListNode(9)
        b = LinkedListNode(7)
        c = LinkedListNode(6)
        d = LinkedListNode(5)
        e = LinkedListNode(4)
        f = LinkedListNode(3)
        g = LinkedListNode(2)
        # List 1: 679
        a.next = b
        b.next = c
        # List 2: 2345
        d.next = e
        e.next = f
        f.next = g
        # Sum:
        h = sum_lists(a, d)
        print(h.value, h.next.value, h.next.next.value, h.next.next.next.value)

if __name__ == '__main__':
    unittest.main()
