from imports import *

# Problem variables
n = 8

# Create the problem instance
problemInstance = ProblemInstance(n)
problemInstance.generateInstance()

# Genetic algorithm variables
selectionMethod = tournamentSelection
crossoverMethod = orderCrossover
mutationMethod = inversion
elitismMethod = conditionalElitism
populationSize = 100
mutationRate = 0.01
elitismRate = 0.01
generations = 30

# Create and run the genetic algorithm
geneticAlgorithm = GeneticAlgorithm(problemInstance, selectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)

geneticAlgorithmOutput = geneticAlgorithm.run()
geneticAlgorithmSolution = geneticAlgorithmOutput[-1]['min']

# Results
applyBruteForce = True # Not recommended for large values of n

print('\n----------> Output <----------\n')
printGAOutput(geneticAlgorithmOutput)

print('\n----------> Solutions <----------')

print(f'\nGenetic algorithm solution:')
print(geneticAlgorithmSolution)

if applyBruteForce:
    bruteForceSolution = (problemInstance.bruteForce())

    print(f'\nBrute force solution:')
    print(f'Fitness: {bruteForceSolution[1]}, Permutation: {bruteForceSolution[0]}')
