def dijkstra(graph, start, finish, verbose = False):
    if verbose:
        print(f"Shortest path from node {start} to node {end}")
    
    # Initialize all the nodes to an impossible value. "Value" is the length of the shortest path from the start node.
    node_values = {}
    starting_node_value = "unknown"
    for node in graph.nodes():
        node_values[node] = starting_node_value

    # Initialize the first node 
    node_values[start] = 0

    # Initialize a list of nodes still remaining to be processed
    nodes_still_to_process = [node for node in graph.nodes()]

    # Dictionary to keep information about the path we follow through the graph
    reverse_children = {}

    # processing_node will be updated every cycle to be a new node
    # Initialize it now to the starting node
    processing_node = start
    processing_node_value = node_values[start]

    while len(nodes_still_to_process) > 0:
        # Process neighbouring edges
        neighbours = [neighbour for neighbour in graph.neighbors(processing_node) if neighbour in nodes_still_to_process]

        for neighbour in neighbours:
            possible_neighbour_value = processing_node_value + int(graph.get_edge_data(processing_node, neighbour)["weight"])

            if is_lower_value(possible_neighbour_value, node_values[neighbour]):
                # If it's a lower value (i.e., a shortest path)
                # 1 Update the value in node_values
                # 2 Save the fact that we reached the new node from processing_node
                if verbose:
                    print(f"Updated node {neighbour} value to {possible_neighbour_value} from {node_values[neighbour]}")

                node_values[neighbour] = possible_neighbour_value
                reverse_children[neighbour] = processing_node

        
        # We're finished with this node, mark it as processed
        nodes_still_to_process.remove(processing_node)

        # If appending that node means we're done with the node list, break inmediately
        if len(nodes_still_to_process) == 0:
            break

        # Choose a new node to process by searching for the lowest node value
        minimum_node = nodes_still_to_process[0]
        minimum_node_value = node_values[minimum_node]

        for node in nodes_still_to_process: 
            if is_lower_value(node_values[node], minimum_node_value):
                minimum_node = node
                minimum_node_value = node_values[node]
        
        # At the end of the loop, we have the node with the lowest value
        if verbose:
            print(f"Finished with node {processing_node}")
            print(f"Will process node {minimum_node} next")

        # Update loop variables
        processing_node = minimum_node
        processing_node_value = minimum_node_value

    # Get the path we followed with the information stored in reverse_children
    reverse_path = [end]
    track_node = end
    while track_node in reverse_children:
        reverse_path.append(reverse_children[track_node])
        track_node = reverse_children[track_node]

    reverse_path.reverse() 

    # Returns: Node value of the final node (the length of the shortest path from start to finish), 
    # the path followed to reach it, node values of all nodes
    return node_values[finish], reverse_path, node_values

def is_lower_value(value1, value2):
    # Returns True is value1 is lower than value2
    # False if value1 is higher or equal
    try:
        value2 = int(value2)
    except:
        # Can't cast to int. value1 will always be lower or equal to value2
        return True
    
    try:
        value1 = int(value1)
    except:
        # Opposite the case above
        return False
    
    # If both are numbers, we can evaluate them as normal
    return value1 < value2