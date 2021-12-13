#!/usr/bin/env python3.9
#@Author: Murtadha Marzouq
#@Date:   2021-12-16
#@Last Modified by:   Murtadha Marzouq
#@description: Shortest Path Algorithm

import matplotlib.pyplot as plt
import networkx as nx
from networkx.utils.random_sequence import weighted_choice
from numpy import add

# Add an edge to the graph    
def add_edge(graph, u, v, w):
    graph[u].append(v)
    graph[v].append(u)
    if w:
        graph[u].append(w)
        graph[w].append(u)



    
def dijkstra(graph, start, weight):
    dist = {}
    prev = {}
    for v in graph:
        dist[v] = float("inf")
        prev[v] = None
    dist[start] = 0
    Q = []
    for v in graph:
        Q.append(v)
    while Q:
        u = min(Q, key=lambda x: dist[x])
        Q.remove(u)


# define a graph with edges and weights
nodes =  ['U', 'V', 'X', 'Z', 'S', 'W', 'Y', 'T'] 
edges = [('U', 'V', 3), ('U', 'W', 2)
         , ('V', 'X',1 ),  ('V', 'Y',2), 
         ('W', 'S',4), ('W', 'X',1),
         ('S', 'T',3), ('X', 'T',5), 
         ('X', 'V', 1)  , ('X', 'Z',4 )
         , ('Y', 'Z',1), ('Y', 'V', 2),]


def my_algorithms(graph, start):
    visited = {}
    unvisited = graph.nodes
    
# create a graph with edges and weights

G = nx.Graph()
G.is_weighted = True
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)



plt.figure(figsize=(7,7))

nx.draw(G, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue', edge_color='black', font_size=10, width=1, alpha=0.5, linewidths=1)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=nx.get_edge_attributes(G, 'weight'))


print(G) 
plt.show()
