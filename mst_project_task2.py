#MST using Kruskal's Algorithm
#Andreea Dobre 26/10/2026
#task 2 for DSA2

"""
Minimum Spanning Tree
Algorithm: Kruskal's algorithm with Disjoint Set Union (Union-Find).

Install dependencies:
    pip install networkx matplotlib

Run:
    mst_project_task2.py
"""

import networkx as nx
import matplotlib.pyplot as plt


#function definition
def MyMinimumSpanningTree(Graph) -> nx.Graph:
    """Return an MST of a connected, undirected, weighted NetworkX graph.
    Kruskal's algorithm is implemented directly (not delegated to NetworkX).
    Edge weights are read from the 'weight' attribute; missing weights default
    to 1, matching NetworkX's usual MST convention.
    """
    #input validation checks (graph undirected, not empty and connected)
    #if the condition is not true, the 'raise' stop the execution and report an error
    if Graph.is_directed():
        raise ValueError("Graph must be undirected.")
    if len(Graph) == 0:
        raise ValueError("Graph must contain at least one node.")
    if not nx.is_connected(Graph):
        raise ValueError("Graph must be connected.")

    #creating the union-find (data structure/disjoint-set to avoid creating cycles)
    #the next 2 lines are two phyton dicitonaries
    #node:node for node = for each node, it stores the node itself as its parent
    #rank = initially each node rank is 0; estimate the depth of a group internal tree and will be used to decide which group will become parent in a merge of 2 groups
    parent = {node: node for node in Graph.nodes()}
    rank = {node: 0 for node in Graph.nodes()}

    #creating the function find; nested function to find root node of a group containing a node
    #this function check if 2 nodes alredy belong to the same connected component of the selected edges
    def find(node):
        # Path compression
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    #creating the funciton union; this merges groups when an edge is accepted
    def union(a, b):
        #find the representative root of each endpoint
        root_a, root_b = find(a), find(b)
        #check if nodes are already connected
        if root_a == root_b:
            return False
        # Union by rank
        #If A's group's root has a smaller rank, make it a child of B's group's root
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        #If A's group's root has a larger rank, make B's group's root a child of A's.
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        #If the ranks are equal, attach B's root under A's root and increase A's rank by one.
        else:
            parent[root_b] = root_a
            rank[root_a] += 1
        return True

    #creating the mst based on find_union
    mst = nx.Graph()
    #adding all the nodes from the original graph
    mst.add_nodes_from(Graph.nodes(data=True))
    #sorting and selection of edges
    sorted_edges = sorted(
        Graph.edges(data=True),
        key=lambda edge: edge[2].get("weight", 1)
    )

    #main alg loop
    print("\nKruskal's algorithm: edges considered in ascending weight order")
    print("Decision log:")
    #u=first node, v=second node, data = edge attribute including weight
    for u, v, data in sorted_edges:
        #extracts the weight using 1 if no weight is present, store it in this new variable
        weight = data.get("weight", 1)
        #calling for union function
        #if return true - they are in different groups so edge accepted
        #if return false - nodes already connected and edge will create cycle
        if union(u, v):
            mst.add_edge(u, v, **data)
            print(f"  ACCEPT  {u} - {v} (weight {weight}); MST edges = {mst.number_of_edges()}")
        else:
            print(f"  REJECT  {u} - {v} (weight {weight}); would create a cycle")
        #stopping the loop when v-1 edges are accepted
        if mst.number_of_edges() == len(Graph.nodes()) - 1:
            break

    #calculating the total weight and returning the mst
    #storing the total of the weights in new var total
    #in order: retrive edge weight and looping over each edge (_ means we don't need to use 2 endpoints variables) after returning all mst edges with their attributes
    total = sum(data.get("weight", 1) for _, _, data in mst.edges(data=True))
    print(f"MST: {mst.number_of_edges()} edges, total weight = {total}")
    #returning the mst
    return mst


#drawing the graphs with Matplotlib
def draw_graph(graph, title, filename, pos):
    plt.figure(figsize=(8, 5.5))
    nx.draw_networkx(
        graph, pos, with_labels=True, node_size=850,
        node_color="lightblue", edge_color="black",
        font_size=10, font_weight="bold", width=1.7
    )
    labels = {(u, v): data.get("weight", 1)
              for u, v, data in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=10)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename, dpi=180, bbox_inches="tight")
    plt.show()
    plt.close()


#creating the graphs
def make_graphs():
    # Graph 1: 6 nodes and 11 edges
    G1 = nx.Graph()
    G1.add_weighted_edges_from([
        ("A", "B", 4), ("A", "C", 3), ("A", "D", 8),
        ("B", "C", 2), ("B", "D", 5), ("B", "E", 7),
        ("C", "D", 6), ("C", "E", 9), ("C", "F", 10),
        ("D", "E", 1), ("E", "F", 4)
    ])

    # Graph 2: 5 nodes, 8 edges, different topology and weights
    G2 = nx.Graph()
    G2.add_weighted_edges_from([
        (1, 2, 6), (1, 3, 2), (1, 4, 7), (2, 3, 4),
        (2, 5, 3), (3, 4, 5), (3, 5, 8), (4, 5, 1)
    ])

    # Graph 3: 7 nodes, 10 edges, different from both previous graphs
    G3 = nx.Graph()
    G3.add_weighted_edges_from([
        ("P", "Q", 3), ("P", "R", 8), ("Q", "R", 2),
        ("Q", "S", 6), ("R", "S", 5), ("R", "T", 7),
        ("S", "T", 1), ("S", "U", 9), ("T", "U", 4),
        ("U", "V", 2)
    ])
    #test all 3 graphs in the same code
    return [G1, G2, G3]


#running and testing everything
#defining main function
def main():
    #calls previous function, make_graphs and stores the returned list in new var
    graphs = make_graphs()
    #looping over each graph created, stating at 1 because graph is corresponding nx graph
    for index, graph in enumerate(graphs, start=1):
        #check if each graph is connected
        assert nx.is_connected(graph)
        #check graph size (as per assignmnent requests)
        if index == 1:
            assert graph.number_of_nodes() == 6
            assert graph.number_of_edges() == 11
        else:
            assert graph.number_of_nodes() >= 5
            assert graph.number_of_edges() >= 8

        print("\n" + "=" * 60)
        print(f"GRAPH {index}: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges")
        pos = nx.spring_layout(graph, seed=100 + index)
        draw_graph(graph, f"Graph {index}: original weighted graph", f"graph{index}_original.png", pos)

        #passing the current graph trough the alg and stores the returned MST in mst var
        mst = MyMinimumSpanningTree(graph)
        # independent verification against nx built-in Kruskal MST.
        reference = nx.minimum_spanning_tree(graph, algorithm="kruskal")
        #frozenset represent each edge without depending on an endpoint order
        #set compare collections of edges
        assert set(map(frozenset, mst.edges())) == set(map(frozenset, reference.edges()))
        #check for V-1 condition for MST
        assert mst.number_of_edges() == graph.number_of_nodes() - 1
        #check if it is a tree: connected and no cycles
        assert nx.is_tree(mst)
        #check if total weight of MST is the same with one from nx
        assert sum(d["weight"] for _, _, d in mst.edges(data=True)) == \
               sum(d["weight"] for _, _, d in reference.edges(data=True))

        #printing independant verification
        print("Verification passed: connected tree, V-1 edges, same minimum total weight as NetworkX reference.")
        print("MST edges:", sorted(
            [(str(u), str(v), d["weight"]) for u, v, d in mst.edges(data=True)]
        ))
        #drawing and saving the MST using the same node positions as the original graph
        draw_graph(mst, f"Graph {index}: minimum spanning tree", "graph{index}_mst.png", pos)

    #message for all 3 tests of 3 graphs
    print("\nALL THREE TESTS PASSED.")


#reuse of the function main without automatically running all the tests
if __name__ == "__main__":
    main()
