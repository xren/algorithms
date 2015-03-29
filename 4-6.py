# write a function to find the next node of a given node in BST


def getNext(root):
    if root == root.parent.left:
        if not root.right:
            return root.parent
        else:
            return getLeftMost(root.right)
    elif root == root.parent.right:
        if not root.right:
            parent = root.parent
            if not parent.parent:
                return None
            while parent != parent.parent.left:
                if not parent.parent:
                    return None
                parent = parent.parent
            return parent.parent
        else:
            return getLeftMost(root.right)
    else:
        return getLeftMost(root)

def getLeftMost(root):
    if not root:
        return

    if not root.left:
        return root

    current = root
    while current.left:
        current = current.left

    return current
