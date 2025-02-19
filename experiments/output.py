import csv

# Prints the output of the genetic algorithm
def printGAOutput(output):
    for generation in output:
        print(f'Generation {generation["generation"]}:')

        print(f'Individual with lowest cost: {generation["min"]}')
        print(f'Individual with highest cost: {generation["max"]}')
        print(f'Average cost: {generation["avg"]}')
        print()

# Writes the problem instance to a file
def writeProblemInstanceToFile(instance, filename):
    with open (filename, 'w') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['Problem instance'])
        writer.writerow(['Locations', 'Distance Matrix', 'Weight Matrix'])
        # Write the data
        writer.writerow([instance.locations, instance.distanceMatrix, instance.weightMatrix])

# Writes the output of the genetic algorithm to a file
def writeGAOutputToFile(output, filename):
    with open(filename, 'a') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['Genetic algorithm output'])
        writer.writerow(['Generation', 'Minimum Fitness', 'Minimum Permutation', 'Maximum Fitness', 'Maximum Permutation', 'Average Cost'])
        # Write the data
        for generation in output:
            writer.writerow([generation['generation'], generation['min'].fitness, generation['min'].permutation, generation['max'].fitness, generation['max'].permutation, generation['avg']])

# Writes the solution of the genetic algorithm to a file
def writeGASolutionToFile(solution, filename):
    with open (filename, 'a') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['Genetic algorithm solution'])
        writer.writerow(['Fitness', 'Permutation'])
        # Write the data
        writer.writerow([solution.fitness, solution.permutation])
