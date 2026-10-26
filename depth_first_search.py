def depth_first_search(graph, target_node, starting_node, previous_node = None, verbose = False):

    # Consumes a nx.Graph object
    # The graph has to be a rooted tree, does not support cycles
    # Searches for target_node in graph using a depth first strategy
    # Returns the path to find the searched for node from the starting node
    # Returns null if no path found

    # previous_node used during recursion, leave as None on first call
    # verbose for extra stdout output
    
    if verbose:
        print("Searching in subtree starting at node " + str(starting_node))

    # If this node is the one we're looking ofr, return it in a list
    if starting_node == target_node:
        if verbose:
                print("Found node")
        return [starting_node]

    # Get the children as: Any nodes connected to starting_node that are not previous_node, as we don't want to go back yet
    children = [neighbour for neighbour in graph.neighbors(starting_node) if neighbour != previous_node]

    for child in children:
        # Recursive call
        child_result = depth_first_search(graph, target_node, child, previous_node = starting_node, verbose = verbose)
        if child_result is not None:
            # If the child call returns a successful result (any number of steps deep) we trace the path backwards to the root
            if previous_node is None:
                # previous_node is only empty on the very first call. So if it's empty,
                # append this node, reverse the list, and then return it
                child_result.append(starting_node)
                child_result.reverse()
                return child_result
            else:
                # If previous node is not empty, it's one of the intermediate recursive calls
                # Append to the list and return it without reversing
                child_result.append(starting_node)
                return child_result
                
    if verbose:
        print("Node not found in children, going back")
    # If this is reached, none of the children returned a result (or there are no children)
    # Return an empty result
    return