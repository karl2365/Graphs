
def earliest_ancestor(ancestors, starting_node):
    stack = []
    visited = set()
    stack.append([starting_node])  
    maxList = []

    while len(stack) > 0:
        path = stack.pop()  
        v = path[-1]  

        if v not in visited:
            visited.add(v) 
            
            for neighbors in ancestors:
                if v == neighbors[-1]: 
                    # update max if longer
                    current = [*path, neighbors[0]]
                    if len(current) > len(maxList):
                        maxList = [*current]
                    # get smaller number if equal
                    if len(current) == len(maxList):
                        if current[-1] < maxList[-1]:
                            maxList = [*current]
                    stack.append(current)
                    
    if len(maxList) == 0:
        return -1
    return maxList[-1]

