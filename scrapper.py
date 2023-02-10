import praw

# Initialize the Reddit instance
reddit = praw.Reddit(client_id='jQYJtpYC2i-2Mtg_DvBuYA',
                     client_secret='g1F0T2PVzYONFYisl86SsbIn-ct-dw',
                     username='vivekmalipatel23',
                     password='@Hbhq2sur',
                     user_agent='OnlineSocialNetworkAnalysis_Project1')

# Choose a subreddit to crawl data from
subreddit = reddit.subreddit('your_subreddit')

# Get a list of users from the subreddit
users = []
for submission in subreddit.hot(limit=500):
    author = submission.author
    if author not in users:
        users.append(author)

# Create a dictionary to store the relationships between users
friendship_network = {user: {'followers': [], 'followees': []} for user in users}

# Loop through the list of users and get their followers and followees
for user in users:
    for follower in user.followers():
        if follower in users:
            friendship_network[user]['followers'].append(follower)
    for followee in user.following():
        if followee in users:
            friendship_network[user]['followees'].append(followee)

# The friendship_network dictionary now contains the data for the friendship network
# representation with around 100-500 nodes
