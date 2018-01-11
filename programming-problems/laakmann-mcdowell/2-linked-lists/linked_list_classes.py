"""
Linked Lists in Python

Taken from InterviewCake August 2016
"""


class LinkedListNode(object):
    """Singly Linked List Node"""

    def __init__(self, value):
        super(LinkedListNode, self).__init__()
        self.value = value
        self.next = None


# Build a singly linked list

a = LinkedListNode(5)
b = LinkedListNode(1)
c = LinkedListNode(9)

a.next = b
b.next = c

class DLinkedListNode():
	"""Doubly Linked List Nodes"""
	def __init__(self, arg):
#		super(DLinkedListNode, self).__init__()
		self.arg = arg
		self.next = None
		self.previous = None
		
# Build a doubly linked list

# Put b after a
a.next = b
b.previous = a

# Put c after b
b.next = c
c.previous = b

