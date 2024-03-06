pip install streamlit pandas
import streamlit as st
import pandas as pd
import math

def distance_between(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_between(route[i], route[i+1])
    return total_distance

def two_opt(route):
    best_route = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 1):
            for j in range(i + 1, len(route)):
                new_route = best_route[:i] + best_route[i:j][::-1] + best_route[j:]
                if calculate_distance(new_route) < calculate_distance(best_route):
                    best_route = new_route
                    improved = True
    return best_route

def main():
    st.title("2-Opt TSP Solver")

    # Input coordinates using a Streamlit DataFrame
    st.header("Enter Coordinates:")
    df = pd.DataFrame(columns=['X', 'Y'])
    for i in range(5):  # Change this number based on your number of points
        x = st.number_input(f"Point {i+1} - X:", value=0.0)
        y = st.number_input(f"Point {i+1} - Y:", value=0.0)
        df = df.append({'X': x, 'Y': y}, ignore_index=True)

    # Convert DataFrame to a list of tuples
    route = list(zip(df['X'], df['Y']))

    # Optimize the route
    optimized_route = two_opt(route)

    # Display the optimized route on the map
    st.header("Optimized Route:")
    st.map(optimized_route)

if __name__ == "__main__":
    main()
