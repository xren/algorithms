# You are given a binary tree in which each node contains a value. Design an algorithm
# to print all paths which sum to a given value. Note that a path can start or end anywhere
# in the tree

def findSum(root, sumValue, path, level):
    if not root:
        return

    path[level] = root.value

    currentSum = 0
    for index, value in enumerate(reverse(path)):
        currentSum += i
        if currentSum == sumValue:
            print path[index:]

    findSum(root.left, sumValue, path, level+1)
    findSum(root.right, sumValue, path, level+1)

    path = []







findSum(root, sumValue, [], 0)
