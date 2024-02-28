from math import factorial

def count_traffic_light_permutations(n):
    return factorial(n)

# Example usage:
num_traffic_lights = 4
permutations = count_traffic_light_permutations(num_traffic_lights)
print("Number of permutations of traffic light arrangement:", permutations)
