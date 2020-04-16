
def earliest_ancestor(ancestors, starting_node):
    stack = []
    visited = set()
    stack.append([starting_node])  # [ [2] ]
    maxList = []
    while len(stack) > 0:
        path = stack.pop()  # [2]
        v = path[-1]  # 2
        if v not in visited:
            visited.add(v)  # { 2 }
            for neighbors in ancestors:
                if v == neighbors[-1]:  # 2 != neighbors.. False
                    current = [*path, neighbors[0]]
                    if len(current) > len(maxList):
                        maxList = [*current]
                    if len(current) == len(maxList):
                        if current[-1] < maxList[-1]:
                            maxList = [*current]
                    stack.append(current)
    # since line 13 is False, maxList never gets updated since it doesnt have a parent.
    if len(maxList) == 0:
        return -1
    return maxList[-1]

