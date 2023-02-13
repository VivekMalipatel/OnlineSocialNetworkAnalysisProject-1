import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# read the edge list from the csv file
df_edges = pd.read_csv('/Users/vivekmalipatel/Downloads/Assignmnts/OSNA/edges.csv')

# create a graph from the edge list
G = nx.from_pandas_edgelist(df_edges, 'user1', 'user2')

# calculate the degree distribution and plot it as a histogram
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = pd.Series(degree_sequence).value_counts()
degree_count.sort_index(inplace=True)
plt.bar(degree_count.index, degree_count.values)
plt.title('Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('Count')
plt.show()

# calculate the clustering coefficient and betweenness centrality
clustering = nx.clustering(G)
betweenness = nx.betweenness_centrality(G)

# plot the distribution of clustering coefficients
clustering_count = pd.Series(clustering).value_counts()
clustering_count.sort_index(inplace=True)
plt.bar(clustering_count.index, clustering_count.values)
plt.title('Distribution of Clustering Coefficients')
plt.xlabel('Clustering Coefficient')
plt.ylabel('Count')
plt.show()

# plot the distribution of betweenness centrality
betweenness_count = pd.Series(betweenness).value_counts()
betweenness_count.sort_index(inplace=True)
plt.bar(betweenness_count.index, betweenness_count.values)
plt.title('Distribution of Betweenness Centrality')
plt.xlabel('Betweenness Centrality')
plt.ylabel('Count')
plt.show()
