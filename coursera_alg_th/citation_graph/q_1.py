import matplotlib.pyplot as plt
import seaborn as sns
import requests
import degree_dist_main
import graph_url_load

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

citation_graph = graph_url_load.load_graph(CITATION_URL)

degree_dist_graph = degree_dist_main.in_degree_distribution(citation_graph)
degree_norm_graph = degree_dist_main.normalizing_graph(degree_dist_graph)
# print(degree_norm_graph)

lists = sorted(degree_norm_graph.items())
degree, value = zip(*lists)
plt.figure(dpi=300)
plt.loglog(degree, value)
plt.xlabel('Degree (Log)')
plt.ylabel('Normalized distribution (Log)')
plt.show()
