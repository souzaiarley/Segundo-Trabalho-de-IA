from geneticAlgorithm import *

# Problem variables
n = 8

# Create the problem instance
problemInstance = ProblemInstance(n)
problemInstance.generateInstance()

# Genetic algorithm variables
selectionMethod = tournamentSelection
crossoverMethod = orderCrossover
mutationMethod = inversion
elitismMethod = pureElitism
populationSize = 500
mutationRate = 0.01
elitismRate = 0.01
generations = 30

# Create and run the genetic algorithm
geneticAlgorithm = GeneticAlgorithm(problemInstance, selectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)

geneticAlgorithmSolution = geneticAlgorithm.run()

# Results
applyBruteForce = True # Not recommended for large values of n

print('\n----------> Solution <----------')

print(f'\nGenetic algorithm solution:')
print(geneticAlgorithmSolution)

if applyBruteForce:
    bruteForceSolution = (problemInstance.bruteForce())

    print(f'\nBrute force solution:')
    print(f'Fitness: {bruteForceSolution[1]}, Permutation: {bruteForceSolution[0]}')
