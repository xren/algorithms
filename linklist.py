class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def printAll(self):
        node = self
        while node:
            print node.value
            node = node.next
