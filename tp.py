import streamlit as st
import copy

# Define the distance array for 5 points
distance_matrix = [
    [0, 10, 15, 20, 5],
    [10, 0, 25, 30, 15],
    [15, 25, 0, 18, 22],
    [20, 30, 18, 0, 28],
    [5, 15, 22, 28, 0]
]

# Function to calculate the total distance of a tour
def total_distance(tour):
    total = 0
    for i in range(len(tour) - 1):
        j = i + 1
        total += distance_matrix[tour[i]][tour[j]]
    total += distance_matrix[tour[0]][tour[-1]]  # Add distance from last to first point
    return total

# Function to implement the 2-opt swap
def two_opt_swap(tour, i, j):
    new_tour = copy.deepcopy(tour)
    sub_tour = new_tour[i:j + 1]
    sub_tour.reverse()
    new_tour[i:j + 1] = sub_tour
    return new_tour

# Streamlit app
st.title("2-Opt Algorithm for Tour Optimization")

st.subheader("Distance Matrix")
st.table(distance_matrix)

# Sidebar to input initial tour
initial_tour_input = st.sidebar.text_input(
    "Write Initial Tour (Separate by spaces):", key="initial_tour"
)

# Combine and validate user input (if provided)
if initial_tour_input:
    try:
        # Validate input format (numbers separated by spaces)
        initial_tour = list(map(int, initial_tour_input.split()))
        if len(initial_tour) != len(distance_matrix):
            raise ValueError("Invalid input: Number of values must match number of points.")
    except ValueError as e:
        st.error(f"Error: {e}")
        initial_tour = []  # Reset invalid input
else:
    initial_tour = []  # Empty tour if no input

if initial_tour:  # Display initial tour only if provided
    st.subheader("Initial Tour")
    st.write(" ".join(map(str, initial_tour)))

# Run button to trigger optimization
if st.button("Optimize Tour"):
    # Prioritize user-provided initial tour (if valid)
    if initial_tour:
        initial_tour = [i for i in initial_tour]  # Ensure list type
    else:
        initial_tour = [i for i in range(len(distance_matrix))]  # Default initial tour

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

    # Display results
    st.subheader("Optimized Tour")
    st.write(" ".join(map(str, initial_tour)))
    st.subheader("Total Distance")
    st.write(total_distance(initial_tour))
