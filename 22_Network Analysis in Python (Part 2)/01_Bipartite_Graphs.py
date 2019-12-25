# Bipartite graphs
# The bipartite keyword
# In the video, Eric introduced you to the 'bipartite' keyword. This keyword is part of a node's metadata dictionary, and can be assigned both when you add a node and after the node is added. Remember, though, that by definition, in a bipartite graph, a node cannot be connected to another node in the same partition.
# Here, you're going to write a function that returns the nodes from a given partition in a bipartite graph. In this case, the relevant partitions of the Github bipartite graph you'll be working with are 'projects' and 'users'.
# Define get_nodes_from_partition()
def get_nodes_from_partition(G, partition):
    # Initialize an empty list for nodes to be returned
    nodes = []
    # Iterate over each node in the graph G
    for n in G.nodes():
        # Check that the node belongs to the particular partition
        if G.node[n]['bipartite'] == partition:
            # If so, append it to the list of nodes
            nodes.append(n)
    return nodes

# Print the number of nodes in the 'projects' partition
print(len(get_nodes_from_partition(G, 'projects')))

# Print the number of nodes in the 'users' partition
print(len(get_nodes_from_partition(G, 'users')))

# It looks like the 'projects' partition has 11774 nodes, while the 'users' partition has 10677 nodes!

# Degree centrality distribution of user nodes
# In this exercise and the next one, you're going to do a final recap of material from the previous course. Your task is to plot the degree centrality distributions for each node partition in the bipartite version of the GitHub collaboration network. Here, you'll do this for the 'users' partition. In the next exercise, you'll do this for the 'projects' partition.

# The function you wrote before, get_nodes_from_partition(), has been loaded for you. Just to remind you, the "degree centrality" is a measure of node importance, and the "degree centrality distribution" is the list of degree centrality scores for all nodes in the graph. A few exercises ago, when you made the circos plot, we computed the degree centralities for you. You'll now practice doing this yourself!
# Import matplotlib
import matplotlib.pyplot as plt

# Get the 'users' nodes: user_nodes
user_nodes = get_nodes_from_partition(G,'users')

# Compute the degree centralities: dcs
dcs = nx.degree_centrality(G)

# Get the degree centralities for user_nodes: user_dcs
user_dcs = [dcs[n] for n in user_nodes]

# Plot the degree distribution of users_dcs
plt.yscale('log')
plt.hist(user_dcs, bins=20)
plt.show()

# Degree centrality distribution of project nodes
# Now it's time to plot the degree centrality distribution for the 'projects' partition of G. The steps to do this are exactly the same as in the previous exercise. For your convenience, matplotlib.pyplot has been pre-imported as plt.

# Go for it!
# Get the 'projects' nodes: project_nodes
project_nodes = get_nodes_from_partition(G,'projects')

# Compute the degree centralities: dcs
dcs = nx.degree_centrality(G)

# Get the degree centralities for project_nodes: project_dcs
project_dcs = [dcs[n] for n in project_nodes]

# Plot the degree distribution of project_dcs
plt.yscale('log')
plt.hist(project_dcs, bins=20)
plt.show()

# Shared nodes in other partition
# In order to build up your concept of recommendation systems, we are going to start with the fundamentals. The focus here is on computing user similarity in bipartite graphs.

# Your job is to write a function that takes in two nodes, and returns the set of repository nodes that are shared between the two user nodes.

# You'll find the following methods and functions helpful in this exercise - .neighbors(), set(), and .intersection() - besides, of course, the shared_partition_nodes function that you will define!
def shared_partition_nodes(G,node1,node2):
    # Check that the nodes belong to the same partition
    assert G.node[node1]['bipartite'] == G.node[node2]['bipartite']

    # Get neighbors of node 1: nbrs1
    nbrs1 = G.neighbors(node1)
    # Get neighbors of node 2: nbrs2
    nbrs2 = G.neighbors(node2)

    # Compute the overlap using set intersections
    overlap = set(nbrs1).intersection(nbrs2)
    return overlap

# Print the number of shared repositories between users 'u7909' and 'u2148'
print(len(shared_partition_nodes(G,'u7909','u2148')))
# <script.py> output:
    # {'p299', 'p607', 'p2000'}
#  It looks like there are 3 repositories shared between users 'u7909' and 'u2148'

# User similarity metric
# Having written a function to calculate the set of nodes that are shared between two nodes, you're now going to write a function to compute a metric of similarity between two users: the number of projects shared between two users divided by the total number of nodes in the other partition. This can then be used to find users that are similar to one another.
def user_similarity(G, user1, user2, proj_nodes):
    # Check that the nodes belong to the 'users' partition
    assert G.node[user1]['bipartite'] == 'users'
    assert G.node[user2]['bipartite'] == 'users'

    # Get the set of nodes shared between the two users
    shared_nodes = shared_partition_nodes(G, user1, user2)

    # Return the fraction of nodes in the projects partition
    return len(shared_nodes) / len(project_nodes)

# Compute the similarity score between users 'u4560' and 'u1880'
project_nodes = get_nodes_from_partition(G, 'projects')
similarity_score = user_similarity(G, 'u4560', 'u1880', project_nodes)

print(similarity_score)
# It looks like these two users are not very similar!

# Find similar users
# You're now going to build upon what you've learned so far to write a function called most_similar_users() that finds the users most similar to another given user.

# The beginnings of this function have been written for you. A list of nodes, user_nodes has been created, which contains all of the users except the given user that has been passed into the function. Your task is to complete the function such that it finds the users most similar to this given user. You'll make use of your user_similarity() function from the previous exercise to help do this.

# A dictionary called similarities has been setup, in which the keys are the scores and the list of values are the nodes. If you've never seen a defaultdict before, don't worry - you'll learn more about it in Chapter 3! It functions exactly like a regular Python dictionary.
from collections import defaultdict

def most_similar_users(G, user, user_nodes, proj_nodes):
    # Data checks
    assert G.node[user]['bipartite'] == 'users'

    # Get other nodes from user partition
    user_nodes = set(user_nodes)
    user_nodes.remove(user)

    # Create the dictionary: similarities
    similarities = defaultdict(list)
    for n in user_nodes:
        similarity = user_similarity(G, user, n, project_nodes)
        similarities[similarity].append(n)

    # Compute maximum similarity score: max_similarity
    max_similarity = max(similarities.keys())

    # Return list of users that share maximal similarity
    return similarities[max_similarity]

user_nodes = get_nodes_from_partition(G, 'users')
project_nodes = get_nodes_from_partition(G, 'projects')

print(most_similar_users(G,'u4560',user_nodes,project_nodes))
# As you can see, the users most similar to 'u4560' are 'u1570' 'u14984', 'u9525', 'u53', 'u363', and 'u2800'.

# Recommend repositories
# You're close to the end! Here, the task is to practice using set differences, and you'll apply it to recommending repositories from a second user that the first user should contribute to.

def recommend_repositories(G, from_user, to_user):
    # Get the set of repositories that from_user has contributed to
    from_repos = set(G.neighbors(from_user))
    # Get the set of repositories that to_user has contributed to
    to_repos = set(G.neighbors(to_user))

    # Identify repositories that the from_user is connected to that the to_user is not connected to
    return set(from_repos).difference(to_repos)

# Print the repositories to be recommended
print(recommend_repositories(G,'u7909','u2148'))
#  The repositories to be recommended to 'u2148' are 'p7408', 'p9312', 'p32418', and 'p66'.