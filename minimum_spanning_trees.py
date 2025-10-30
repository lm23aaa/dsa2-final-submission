"""
minimum_spanning_trees.py

Author: Liam Mills
Created: 2025-10-16
Last Modified: 2025-10-30

Implements functions to work out the minimum spanning trees with famous algorithm(s), and supporting functions
for them.

Dependencies:
    - NetworkX
    - matplotlib

Functions:
    - kruskal(graph: nx.Graph) -> None: Takes a NetworkX connected graph, and creates a minimum spanning tree
    with matplotlib.pyplot.
    - getEdgesWeight(edge) -> None: Takes NetworkX EdgeDataView data and returns the weight from the tuple
    - drawAndShowGraph(G: nx.Graph, edge_color: str, title: str) -> None: Takes a NetworkX graph data and adds styles, before outputting to the screen with matplotlib.pyplot
"""

import networkx as nx
import matplotlib.pyplot as mp

def kruskal(graph: nx.Graph) -> None:
    """
    A function that takes a NetworkX connected graph, and
    creates a minimum spanning tree with matplotlib.pyplot.

    Args:
        - graph (nx.Graph): NetworkX connected graph for the
        function to iterate over while creating a minimum
        spanning tree.

    Side Effects:
        - Prints messages to the console for the user to see.
        - Outputs multiple graphs throughout the program with
        matplotlib.pyplot.
    """

    # state the algoritm being used
    print("The algorithm used to create this Minimum Spanning Tree (MST) is Kruskal's algorithm, and it will be on the following graph.")
        
    # draw the original graph
    drawAndShowGraph(graph, "#0000ff", "Original Connected Graph")

    # Get edges from graph, put them in sorted order
    sorted_edges = sorted(graph.edges(data=True), key=getEdgesWeight)
    
    # Get the amount of nodes in the mst
    mst_node_target = len(graph.nodes())

    # set the mst count to zero
    mst_node_count = 0

    # current weight of the mst
    mst_weight = 0

    # create an empty mst graph
    mst = nx.Graph()

    # title to be output above the graph for context
    mst_title = ""

    # run a loop till the mst_node_count is the same as mst_node_target
    # or, the edges is less than the node_target - 1 (edges = nodes - 1)
    while mst_node_count < mst_node_target or len(mst.edges()) != mst_node_target - 1:
        # Get first element from sorted list
        # desctructure it so the variables are easier to read
        # please note: weight value is inside data
        (node_one, node_two, data) = sorted_edges.pop(0)

        # add to mst 
        mst.add_weighted_edges_from([(node_one, node_two, data["weight"])])

        # check if mst is still a tree
        if nx.is_tree(mst) or nx.is_connected(mst) == False:
            # true, update the node count
            mst_node_count = len(mst.nodes())

            # update the current weight
            mst_weight += data["weight"]

            # update the mst_title
            if mst_node_count == mst_node_target and len(mst.edges()) == mst_node_target - 1:
                mst_title = f"Final MST, weight: {mst_weight}"
            else:
                mst_title = f"Current MST, weight: {mst_weight}"

            # inform the user on the success
            print(f"Edge ({node_one}, {node_two}, weight={data["weight"]}) can be added to the MST.")
        
            # draw the mst at each successful step
            drawAndShowGraph(mst, title=mst_title)
            
        else:
            # false, remove the edge we just added
            mst.remove_edge(node_one, node_two)

            # for each of the nodes connected to our edge
            # we just removed
            for item in [node_one, node_two]:
                # is there an edge left connected to it
                if mst.edges(item):
                    # true, continue to next iteration
                    continue
                else:
                    # false, remove node from mst
                    mst.remove_node(item)

            # update mst node count
            mst_node_count = len(mst.nodes())

            # inform the user on the failure
            print(f"Edge ({node_one}, {node_two}, weight={data["weight"]}) cannot be added to the MST, as it creates a circuit.")

    # print the MST size for the user
    print(f"The final MST weight is {mst_weight}")

    # return None from the function
    return

def getEdgesWeight(edge) -> int:
    """
    A function that takes NetworkX EdgeDataView data and
    returns the weight from the tuple for the sorted function.

    Args:
        - edge (EdgeDataView): NetworkX EdgeDataView data.
    """

    return edge[2].get("weight")

def drawAndShowGraph(G: nx.Graph, edge_color: str = "#ff0000", title: str = "") -> None:
    """
    A function that takes a NetworkX graph data and
    adds styles, before outputting to the screen with
    matplotlib.pyplot.

    Args:
        - G (nx.Graph): NetworkX graph for the
        function style and output.
        - edge_color(str): string to change the colour of the edges,
        with the default being red in hexadecimal.
        - title(str): string to add extra context to the graph.
    """

    if (title != ""):
        mp.title(title)

    # set layout to circular
    pos = nx.circular_layout(G)

    # nodes
    nx.draw_networkx_nodes(G, pos, node_color="#ffffff", node_size=300, edgecolors="#000000", linewidths=1.5)

    # edges
    nx.draw_networkx_edges(G, pos, style="solid", width=2.0, edge_color=edge_color)

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=10)

    # edge labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)

    # output the final graph for the user
    mp.show()

    return


# undirected graph
G = nx.Graph()

# TESTING GRAPH 1
# add nodes
G.add_nodes_from(["a", "b", "c", "d", "e", "f", "g"])

# # add edges
G.add_weighted_edges_from([
    ("a", "b", 53),
    ("a", "c", 33),
    ("a", "d", 51),
    ("b", "c", 5),
    ("b", "e", 39),
    ("c", "d", 98),
    ("c", "f", 12),
    ("d", "e", 49),
    ("e", "f", 15),
    ("e", "g", 8),
    ("f", "g", 19),
])
# TESTING GRAPH 1 END

# TESTING GRAPH 2 
# add nodes
# G.add_nodes_from(["a", "b", "c", "d", "e"])

# # add edges
# G.add_weighted_edges_from([
#     ("a", "b", 196),
#     ("a", "c", 429),
#     ("a", "d", 214),
#     ("a", "e", 374),
#     ("b", "c", 308),
#     ("b", "d", 466),
#     ("b", "e", 112),
#     ("c", "d", 169),
#     ("c", "e", 86),
#     ("d", "e", 225),
# ])
# TESTING GRAPH 2 END

# TESTING GRAPH 3 
# add nodes
# G.add_nodes_from(["a", "b", "c", "d", "e", "z"])

# add edges                      
# G.add_weighted_edges_from([
#     ("a", "b", 22),
#     ("a", "c", 187),
#     ("a", "d", 18),
#     ("a", "e", 175),
#     ("a", "z", 35),
#     ("b", "c", 156),
#     ("b", "d", 146),
#     ("b", "e", 128),
#     ("b", "z", 41),
#     ("c", "d", 34),
#     ("c", "e", 112),
#     ("c", "z", 52),
#     ("d", "e", 88),
#     ("d", "z", 124),
#     ("e", "z", 10),
# ])
# TESTING GRAPH 3 END

# running test from the above
kruskal(G)