# File: k_means_clustering.mod

# Parameters
param n;  # Number of data points
param P;  # Number of possible clusters
param k;  # Number of clusters to select

set I := 1..n;  # Set of data points
set J := 1..P;  # Set of possible clusters

# Parameters
param c{J};  # Cost associated with each cluster
param C{J, I}, binary;  # Binary matrix indicating if a data point is in a cluster

# Decision variable: Binary selection variable for each cluster
var y{J}, binary;  # y[j] = 1 if cluster j is selected, 0 otherwise

# Objective: Minimize total cost of selected clusters
minimize total_cost: sum{j in J} c[j] * y[j];

# Constraints

# Ensure each data point is assigned to exactly one selected cluster
subject to assign_one_cluster{i in I}:
    sum{j in J} C[j, i] * y[j] = 1;

# Limit the number of selected clusters to k
subject to select_k_clusters:
    sum{j in J} y[j] = k;

# Binary constraint on cluster selection
subject to binary_constraints{j in J}:
    0 <= y[j] <= 1;

# Solve the model
solve;

# Output the optimal objective function value
display total_cost;

# Display only the selected clusters
display {j in J: y[j] == 1} y[j];
