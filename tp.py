import streamlit as st
import pandas as pd
import copy
import subprocess

# Function to attempt installing the required libraries
@st.cache
def install_libraries():
    try:
        subprocess.run(["pip", "install", "xlrd", "openpyxl"])
        return True
    except Exception as e:
        st.error(f"Error installing libraries: {e}")
        return False

# Attempt to install the required libraries
if not install_libraries():
    st.error("Error: Both 'xlrd' and 'openpyxl' engines are unavailable.")
else:
    # Function to calculate the total distance of a tour
    def total_distance(tour, distance_matrix):
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

    # File uploader for Excel file
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read the Excel file
        df = pd.read_excel(uploaded_file, index_col=0)

        st.subheader("Distance Matrix")
        st.table(df)

        # Run button to trigger optimization
        if st.button("Optimize Tour"):
            # Default initial tour
            initial_tour = [i for i in range(len(df))]

            # Main optimization loop
            improved = True
            while improved:
                improved = False
                for i in range(1, len(initial_tour) - 2):
                    for j in range(i + 1, len(initial_tour) - 1):
                        new_tour = two_opt_swap(initial_tour, i, j)
                        if total_distance(new_tour, df.values.tolist()) < total_distance(initial_tour, df.values.tolist()):
                            initial_tour = new_tour
                            improved = True

            # Display results
            st.subheader("Optimized Tour")
            st.write(" ".join(map(str, initial_tour)))
            st.subheader("Total Distance")
            st.write(total_distance(initial_tour, df.values.tolist()))
