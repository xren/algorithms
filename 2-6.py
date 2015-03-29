# Given a circular linked list, implement an algorithm which returns the node
# at the begining of the loop

from linklist import Node


def getBegining(head):
    slow = head
    fast = head

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow.value == fast.value:
            break


    slow = head
    while slow.value != fast.value:
        slow = slow.next
        fast = fast.next

    return slow


a = Node(5)
b = Node(4)
c = Node(3)
d = Node(2)

a.next = b
b.next = c
c.next = d
d.next = b

print getBegining(a).value
