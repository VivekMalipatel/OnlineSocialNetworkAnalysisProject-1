import praw
import csv
import networkx as nx
import pickle

# Initialize the Reddit API client
reddit = praw.Reddit(client_id='jQYJtpYC2i-2Mtg_DvBuYA',
                     client_secret='g1F0T2PVzYONFYisl86SsbIn-ct-dw',
                     user_agent='OnlineSocialNetworkAnalysis_Project1')

# Select a subreddit to extract data from
subreddit = reddit.subreddit('all')

