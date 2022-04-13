import matplotlib.pyplot as plt
import requests
import degree_dist_main
import random_graph

random_graph = random_graph.random_graph(0.99, 300)
random_degree_dist = degree_dist_main.in_degree_distribution(random_graph)
random_degree_norm_dist = degree_dist_main.normalizing_graph(random_degree_dist)

lists = sorted(random_degree_norm_dist.items())
degree, value = zip(*lists)
plt.figure(dpi=300)
plt.plot(degree, value)
plt.xlabel('Degree (Log)')
plt.ylabel('Normalized distribution (Log)')
plt.show()
