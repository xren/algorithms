# Given a binary tree, design an algorithm which creates linked list of all the
# nodes at each depth

def getLinkedList(root):
    result = []
    current = getLinkedList()
    if not root:
        current.add(root)

    while current:
        result.append(current)
        parents = current

        currentLinkedList = getLinkedList()
        for parent in parents:
            if parent.left:
                currentLinkedList.add(parent.left)

            if parent.right:
                currentLinkedList.add(parent.right)

    return result
