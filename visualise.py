import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# read the edge list from the csv file
df_edges = pd.read_csv('/Users/vivekmalipatel/Downloads/Assignmnts/OSNA/edges.csv')

# create an empty graph
G = nx.Graph()

# add edges to the graph
for index, row in df_edges.iterrows():
    G.add_edge(row['user1'], row['user2'])

# visualize the graph
pos = nx.spring_layout(G, k=0.15, iterations=20)
nx.draw_networkx_nodes(G, pos, node_color='blue', alpha=0.7)
nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.4)
nx.draw_networkx_labels(G, pos, font_size=8, font_family='Arial')
plt.axis('off')
plt.show()