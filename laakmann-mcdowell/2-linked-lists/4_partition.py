"""
2.4 Partition

Write code to partition a linked list around a value x, such that
all nodes less than x come before all nodes greater than
or equal to x. If x is contained within the list, the values of x
only need to be after the elements less than x. The partition element
x can appear anywhere in the 'right partition'; it does not need to
appear between the left and right partitions.

EXAMPLE:
3->5->8-5->10->2->1 [partition = 5]


"""
from linked_list_classes import LinkedListNode
import unittest



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