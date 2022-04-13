import matplotlib.pyplot as plt
import random_graph
import degree_dist_main
import graph_url_load

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

citation_graph = graph_url_load.load_graph(CITATION_URL)
# dist_graph = degree_dist_main.in_degree_distribution(citation_graph)
out_degree_dict = degree_dist_main.compute_out_degrees(citation_graph)
average_out_degree = sum(out_degree_dict.values()) / len(out_degree_dict.values())

lists = sorted(out_degree_dict.items())
degree, value = zip(*lists)
plt.figure(dpi=300)
plt.plot(degree, value)
plt.xlabel('Degree (Log)')
plt.ylabel('Normalized distribution (Log)')
plt.show()
