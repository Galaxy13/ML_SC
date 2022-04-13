import requests

def load_graph(graph_url):
    """
    This method receives URL of
    text file, in UTF-8 coding.

    Returns graph, presented as library
    and number of nodes, of this graph
    """
    graph_file = requests.get(graph_url)
    graph_text = graph_file.text
    graph_lines = graph_text.split("\n")
    graph_lines = graph_lines[: -1]

    print('Loaded graph with', len(graph_lines), 'nodes')

    answer_graph = {}
    for line in graph_lines:
        neighbours = line.split(' ')
        node = int(neighbours[0])
        answer_graph[node] = set([])
        for neighbour in neighbours[1 : -1]:
            answer_graph[node].add(int(neighbour))

    return answer_graph