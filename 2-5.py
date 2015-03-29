# You have two numbers represented by a linked list, where each node contains a single digit
# The digits are stored in reverse order, such that the 1's digit is at the head of the list
# write a function that adds the two numbers and returns the sum as a linked list
# FOLLOW UPS
# Suppose the digits are stored in forward order. Repeat the above problem

from linklist import Node


def getLength(node):
    count = 0
    while node:
        count += 1
        node = node.next

    return count

def getSum(node1, node2):
    if not node1.next or not node2.next:
        value = node1.value + node2.value
        rest = value % 10
        return (Node(rest), value / 10)

    previousNode, advance = getSum(node1.next, node2.next)
    value = node1.value + node2.value + advance
    rest = value % 10
    node = Node(rest)
    node.next = previousNode
    return (node, value / 10)

def add(head1, head2):
    if not head1 and not head2:
        return

    if not head1:
        return head2

    if not head2:
        return head1

    lengthHead1 = getLength(head1)
    lengthHead2 = getLength(head2)

    shorterNode = head1 if lengthHead1 < lengthHead2 else head2
    longerNode = head1 if lengthHead1 >= lengthHead2 else head2
    difference = abs(lengthHead1 - lengthHead2)

    while difference:
        node = Node(0)
        node.next = shorterNode
        shorterNode = node
        difference -= 1

    head, rest = getSum(shorterNode, longerNode)

    return head

a = Node(5)
b = Node(4)
c = Node(3)
d = Node(2)

a.next = b
b.next = c
c.next = d

e = Node(5)
f = Node(4)
g = Node(3)

e.next = f
f.next = g

node = add(a, e)
node.printAll()
