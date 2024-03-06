import copy

# Define the new distance array for 5 points
new_distance_matrix = [
    [0, 12, 8, 19, 6],
    [12, 0, 21, 14, 28],
    [8, 21, 0, 25, 10],
    [19, 14, 25, 0, 16],
    [6, 28, 10, 16, 0]
]

# Function to calculate the total distance of a tour
def total_distance(tour):
    total = 0
    for i in range(len(tour) - 1):
        j = i + 1
        total += new_distance_matrix[tour[i]][tour[j]]
    total += new_distance_matrix[tour[0]][tour[-1]]  # Add distance from last to first point
    return total

# Function to implement the 2-opt swap
def two_opt_swap(tour, i, j):
    new_tour = copy.deepcopy(tour)
    sub_tour = new_tour[i:j + 1]
    sub_tour.reverse()
    new_tour[i:j + 1] = sub_tour
    return new_tour

# Initial tour (can be any order)
initial_tour = [0, 1, 2, 3, 4]

# Main optimization loop
improved = True
while improved:
    improved = False
    for i in range(1, len(initial_tour) - 2):
        for j in range(i + 1, len(initial_tour) - 1):
            new_tour = two_opt_swap(initial_tour, i, j)
            if total_distance(new_tour) < total_distance(initial_tour):
                initial_tour = new_tour
                improved = True

# Print the optimized tour and its total distance
print("Optimized tour:", initial_tour)
print("Total distance:", total_distance(initial_tour))
