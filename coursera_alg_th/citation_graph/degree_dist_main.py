"""
# Algorithmic Thinking Week 2
# Project # 1: Degree Distributions for Graphs (Machine Grading)
"""

EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 4, 5, 6, 7, 3])}


def make_complete_graph(num_nodes):
    """
    This method receives the number
    of nodes of future graph.

    Returns graph with max degree
    for every node.
    """
    graph_neigbours = set([neighbour for neighbour in range(num_nodes)])
    graph = {}
    for node in range(num_nodes):
        graph_neigbours.remove(node)
        graph[node] = set(graph_neigbours)
        graph_neigbours.add(node)
    return graph


def compute_in_degrees(dict_graph):
    """
    Functions receives graph, represented
    as dictionary in form {node: set([neighbours])}

    Returns dictionary with
    number of edges, corresponding
    to each node {node: in_degree}
    """
    degree_dict = {node: 0 for (node, dummy_value) in dict_graph.items()}
    for edge_set in dict_graph.values():
        for in_edge in edge_set:
            degree_dict[in_edge] += 1
    return degree_dict


def in_degree_distribution(dict_graph):
    """
    Function receives graph, represented
    as dictionary in form {node: set([neighbours])}

    Returns unnormalized distribution
    of nodes degrees as dictionary
    in form {in_degree: count}
    """
    degree_dict = compute_in_degrees(dict_graph)
    count_dict = {count: 0 for count in range(0, max(degree_dict.values()) + 1)}
    for degree in degree_dict.values():
        count_dict[degree] += 1
    return {degree: count for (degree, count) in count_dict.items() if count != 0}

def make_blank_graph(num_nodes):
    return {node: set([]) for node in range(num_nodes)}

def normalizing_graph(dist_graph):
    number_of_edges = sum(dist_graph.values())
    return {key: value / number_of_edges for (key, value) in dist_graph.items()}

def compute_out_degrees(dict_graph):
    out_graph_degrees = {count: 0 for count in range(0, max([len(node_set) for node_set in dict_graph.values()]) + 1)}
    for neighbour_set in dict_graph.values():
        out_graph_degrees[len(neighbour_set)] += 1
    return out_graph_degrees
