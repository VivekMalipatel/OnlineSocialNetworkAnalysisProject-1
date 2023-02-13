import praw
import networkx as nx
import pandas as pd

# create Reddit instance
reddit = praw.Reddit(client_id='2fu6PxfuxVFdSFVGvAdE7A', client_secret='lBd0kynbpVntzKiF5cRXTFtU0S_WxQ', user_agent='OnlineSocialAnalysis')

# get subreddit
subreddit = reddit.subreddit('MachineLearning')

# create empty graph
G = nx.Graph()

# create empty DataFrame to store node and edge data
df_nodes = pd.DataFrame(columns=['user'])
df_edges = pd.DataFrame(columns=['user1', 'user2'])

# iterate through comments
for comment in subreddit.comments(limit=500):
    # get user and parent comment
    user = comment.author
    parent = comment.parent()
    parent_user = None
    
    # check if parent is a comment or a submission
    if isinstance(parent, praw.models.reddit.comment.Comment):
        parent_user = parent.author
    elif isinstance(parent, praw.models.reddit.submission.Submission):
        parent_user = parent.author
        
    # check if user and parent user exist
    if user is not None and parent_user is not None:
        # add nodes and edges to graph and DataFrame
        G.add_node(user)
        G.add_node(parent_user)
        G.add_edge(user, parent_user)
        
        df_nodes = pd.concat([df_nodes, pd.DataFrame({'user': [user]})], ignore_index=True)
        df_nodes = pd.concat([df_nodes, pd.DataFrame({'user': [parent_user]})], ignore_index=True)
        df_edges = pd.concat([df_edges, pd.DataFrame({'user1': [user], 'user2': [parent_user]})], ignore_index=True)

# Store the Dataframes
df_edges.to_csv("edges.csv")
df_nodes.to_csv("nodes.csv")


