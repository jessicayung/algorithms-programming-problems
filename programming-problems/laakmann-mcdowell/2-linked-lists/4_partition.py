"""
2.4 Partition

Write code to partition a linked list around a value x, such that
all nodes less than x come before all nodes greater than
or equal to x. If x is contained within the list, the values of x
only need to be after the elements less than x. The partition element
x can appear anywhere in the 'right partition'; it does not need to
appear between the left and right partitions.

EXAMPLE:
3->5->8->5->10->2->1 [partition = 5]
has possible solution
3->2->1->5->8->5->10

Author: Jessica Yung
16 October 2016

WRITE have-two-lists-(before and after)-that-you-merge version of solution.
"""
from linked_list_classes import LinkedListNode
import unittest

def partition_linked_list(head, partition):
    # partition is a float or an int.
    complete = False
    # For each pass:
    while complete == False:
        # Initialise or reset variables
        current_node = head
        swaps = 0
        prev_prev_node = None
        prev_node = None
        passed_greater_than_partition = 0
        # Loop through nodes
        while current_node is not None:
            # if number >= partition, toggle = 1
            if passed_greater_than_partition == 1 and current_node.value < partition:
                # Swap current node with prev node
                swaps = 1
                if prev_prev_node is not None:
                    # a b c d, c current
                    # a.next = c
                    # b.next = d
                    # c.next = b
                    # a c b d
                    # SWAP
                    prev_prev_node.next = current_node
                    prev_node.next = current_node.next
                    current_node.next = prev_node
                    if prev_node is not None and current_node is not None:
                        print("swapped ", prev_node.value, " with ", current_node.value)
                    # Shift
                    # c current, next current is d.
                else:
                    # a b c, b current
                    # a.next = c
                    # b.next = a
                    # b a c
                    # SWAP
                    prev_node.next = current_node.next
                    current_node.next = prev_node
                    if prev_node is not None and current_node is not None:
                        print("swapped ", prev_node.value, " with ", current_node.value)
                    # SHIFT nodes
                    # current is still b
                    # Next current is c
                    head = current_node
                # Shift nodes
                if current_node.next.next is not None:
                    prev_prev_node = current_node
                    current_node = current_node.next.next
                else:
                    # a b d c
                    current_node = current_node.next
            else:
                if current_node.value >= partition:
                    passed_greater_than_partition = 1
                # No swap
                # Shift nodes
                # a b c d, current is c.
                # Next current is d
                prev_prev_node = prev_node
                prev_node = current_node
                current_node = current_node.next
        # If there were no alterations, we're done
        if swaps == 0:
            complete = True
        if head.next.next.next is not None:
            print(head.value, head.next.value, head.next.next.value, head.next.next.next.value)
    return head

def partition_linked_list_split_solution(head, partition):
    pass

class Tests(unittest.TestCase):
    def test_partition_short(self):
        a = LinkedListNode(9)
        b = LinkedListNode(7)
        c = LinkedListNode(2)
        d = LinkedListNode(1)
        a.next = b
        b.next = c
        c.next = d
        h = partition_linked_list(a, 5)
        print(h, h.next.value, h.next.next.value, h.next.next.next.value)


    def test_partition(self):
        a = LinkedListNode(9)
        b = LinkedListNode(7)
        c = LinkedListNode(6)
        d = LinkedListNode(5)
        e = LinkedListNode(4)
        f = LinkedListNode(3)
        g = LinkedListNode(2)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        f.next = g
        h = partition_linked_list(a, 5)
        fourh = h.next.next.next
        print(h.value, h.next.value, h.next.next.value, fourh.value, fourh.next.value,
              fourh.next.next.value, fourh.next.next.next.value)


if __name__ == '__main__':
    unittest.main()
