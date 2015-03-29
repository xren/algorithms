# an algorithm to delete a node in the middle of a singly linkedlist,
# given only access to that node

# example:
# input the node c from the linked list a - b - c - d - e
# output nothing is returned, but the new linked list looks like a - b - d - e

from linklist import Node

def delete(node):



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

delete(c)

print a.printAll()
