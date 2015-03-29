# Implement a function to check if a binary tree is balanced.

def isBalanced(root):
    if not root:
        return 0

    leftCount = isBalanced(root.left)
    rightCount = isBalanced(root.right)

    if leftCount == False or rightCount == False or abs(leftCount - rightCount) > 1:
        return False

    return max(leftCount, rightCount) + 1
