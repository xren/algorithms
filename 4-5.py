# implement a function to check whether a binary tree is a BST

def isBST(root, minimum, maximum):
    if not root:
        return False

    if root.value > maximum or root.value <= minimum:
        return False

    if root.left and not isBST(root.left, minimum, root.value):
        return False

    if root.right and not isBST(root.right, root.value, maximum):
        return False

    return True
