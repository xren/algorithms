# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree
# Avoid storing additional nodes in a data structure. Note: This is not a bst

def covers(root, p):
    if not root:
        return False

    if root.value == p.value:
        return True

    return covers(root.left, p) || covers(root.right, p)


def getCommonAncestor(root, p, q):
    if root == p:
        return p

    if root == q:
        return q

    isPOnTheLeft = covers(root.left, p)
    isQOnTheLeft = covers(root.left, q)

    if isPOnTheLeft != isQOnTheLeft:
        return root

    if isPOnTheLeft == True:
        return getCommonAncestor(root.left, p, q)
    else:
        return getCommonAncestor(root.right, p, q)
