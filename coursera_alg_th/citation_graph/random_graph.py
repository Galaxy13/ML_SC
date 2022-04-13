import random
import degree_dist_main


def random_graph(probability, nodes):
    blank_graph = degree_dist_main.make_blank_graph(nodes)
    for node in blank_graph.keys():
        node_list = list(blank_graph.keys())
        node_list.remove(node)
        for neighbour in node_list:
            if random.random() < probability:
                blank_graph[node].add(neighbour)
    return blank_graph


def random_dpa_graph(nodes_count, neighbours_subset_len):
    subset_graph = degree_dist_main.make_complete_graph(neighbours_subset_len)
    for node in range(neighbours_subset_len, nodes_count):
        subset = set()
        total_in_degree = sum(degree_dist_main.in_degree_distribution(subset_graph).values())
        probability_list = [(len(value) + 1) / (total_in_degree + len(subset_graph)) for value in subset_graph.values()]
        for dummy_count in range(neighbours_subset_len):
            prob_node = random.choices(population=list(subset_graph.keys()),
                                       weights=probability_list)
            subset.add(prob_node[0])
        subset_graph[node] = subset
    return subset_graph

print(random_dpa_graph(1000, 20))
