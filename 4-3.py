# Given a sorted array, write an algorithm to create a binary search tree with minimal height

def createBST(array):
    if not array or len(array) == 0:
        return

    midIndex = (len(array) - 1) / 2
    mid = array[midIndex]
    root = Node(mid)

    root.left = createBST(array[:midIndex])
    root.right = createBST(array[midIndex+1:])

    return root
