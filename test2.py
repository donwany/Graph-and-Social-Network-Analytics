import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(5)

nx.draw_networkx(G)