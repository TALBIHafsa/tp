def calculate_distance(route):
  # Calculate the total distance of a given route
  def distance_between(a, b):
    # Calculate the distance between two points
    # Replace this with your actual distance calculation logic
    return abs(a - b)

  total_distance = 0
  for i in range(len(route) - 1):
    total_distance += distance_between(route[i], route[i+1])
  return total_distance

def two_opt(route):
  # Perform the 2-opt algorithm using the steepest descent method
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

# Example usage
route = [1, 2, 3, 4, 5]
optimized_route = two_opt(route)
print(optimized_route)
