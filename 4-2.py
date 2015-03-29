# Given a directed graph, design an algorithm to find out whether there is a route between
# two nodes

visited = []

def findRoute(start, end):
    nextNodeList = []
    for node in start.to:
        if node.value == end.value:
            return True
        else:
            if node not in visited:
                result = findRoute(node, end)
                if result == True:
                    return True

    return result
