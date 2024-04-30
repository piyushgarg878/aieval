import random
from __future__ import annotations
from __future__ import annotations

# Define the problem points
points = {
    'A': {'weight': 45, 'value': 3},
    'B': {'weight': 40, 'value': 5},
    'C': {'weight': 50, 'value': 8},
    'D': {'weight': 90, 'value': 10}
}

# Define the parameters
chromosome_length = 4
population_size = 4
max_capacity = 100
mutation_bits = ['D', 'C', 'B', 'A']

# Initialize the population
population = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]

# Function to calculate fitness of a chromosome
def calculate_fitness(chromosome):
    total_weight = 0
    total_value = 0
    for i in range(chromosome_length):
        if chromosome[i] == 1:
            total_weight += points[list(points.keys())[i]]['weight']
            total_value += points[list(points.keys())[i]]['value']
    if total_weight > max_capacity:
        total_value = 0
    return total_value

# Function to perform one-point crossover
def one_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, chromosome_length - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

# Function to perform mutation
def mutate(chromosome):
    mutated_chromosome = chromosome.copy()
    for bit in mutation_bits:
        index = list(points.keys()).index(bit)
        mutated_chromosome[index] = 1 - mutated_chromosome[index]
    return mutated_chromosome

# Perform iterations
for iteration in range(10):
    # Calculate fitness for each chromosome
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]

    # Sort the population based on fitness
    sorted_population = [chromosome for _, chromosome in sorted(zip(fitness_values, population), reverse=True)]

    # Select the fittest chromosomes
    fittest_chromosomes = sorted_population[:2]

    # Perform one-point crossover and mutation
    offspring1, offspring2 = one_point_crossover(fittest_chromosomes[2], fittest_chromosomes[3])
    mutated_offspring1 = mutate(offspring1)

    # Update the population
    population = fittest_chromosomes + [mutated_offspring1, offspring2]

# Output the result
best_chromosome = max(population, key=calculate_fitness)
print("Best chromosome:", best_chromosome)
print("Fitness:", calculate_fitness(best_chromosome))