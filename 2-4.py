# Write code to partition a linked list around a value x, such that all nodes less than x
# come before all nodes greater than or equal to x

from linklist import Node


def partition(node, k):
    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None

    current = node
    kNode = None

    while current:
        nextToCurrent = current.next

        if current.value == k:
            kNode = current
        elif current.value > k:
            if not afterStart:
                afterStart = current
                afterEnd = current
            else:
                afterEnd.next = current
                afterEnd = afterEnd.next

        else:
            if not beforeStart:
                beforeStart = current
                beforeEnd = current
            else:
                beforeEnd.next = current
                beforeEnd = beforeEnd.next

        current.next = None
        current = nextToCurrent

    if beforeStart:
        beforeEnd.next = kNode
        kNode.next = afterStart
        return beforeStart
    else:
        kNode.next = afterStart
        return kNode


a = Node(5)
b = Node(4)
c = Node(3)
d = Node(2)

a.next = b
b.next = c
c.next = d


node = partition(a, 3)
node.printAll()
