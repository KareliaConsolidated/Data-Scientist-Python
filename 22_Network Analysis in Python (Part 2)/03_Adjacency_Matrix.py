# Compute adjacency matrix
# Now, you'll get some practice using matrices and sparse matrix multiplication to compute projections! In this exercise, you'll use the matrix multiplication operator @ that was introduced in Python 3.5.
# You'll continue working with the American Revolution graph. The two partitions of interest here are 'people' and 'clubs'.
# Get the list of people and list of clubs from the graph: people_nodes, clubs_nodes
people_nodes = get_nodes_from_partition(G, 'people')
clubs_nodes = get_nodes_from_partition(G, 'clubs')

# Compute the biadjacency matrix: bi_matrix
bi_matrix = nx.bipartite.biadjacency_matrix(G, row_order=people_nodes, column_order=clubs_nodes)

# Compute the user-user projection: user_matrix
user_matrix = bi_matrix @ bi_matrix.T

print(user_matrix)

# Find shared membership: Transposition
# As you may have observed, you lose the metadata from a graph when you go to a sparse matrix representation. You're now going to learn how to impute the metadata back so that you can learn more about shared membership.

# The user_matrix you computed in the previous exercise has been preloaded into your workspace.

# Here, the np.where() function will prove useful. This is what it does: given an array, say, a = [1, 5, 9, 5], if you want to get the indices where the value is equal to 5, you can use idxs = np.where(a == 5). This gives you back an array in a tuple, (array([1, 3]),). To access those indices, you would want to index into the tuple as idxs[0].
