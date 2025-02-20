import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from experiments.imports import *

# Creating a custom QAP instance
n = 9

locations = [(20, 12), (9, 5), (26, 14), (18, 30), (10, 4), (9, 17), (14, 9), (1, 11), (7, 4), (18, 7)]

distanceMatrix = [
    [0, 13, 6, 18, 12, 12, 6, 19, 15, 5],
    [13, 0, 19, 26, 1, 12, 6, 10, 2, 9],
    [6, 19, 0, 17, 18, 17, 13, 25, 21, 10],
    [18, 26, 17, 0, 27, 15, 21, 25, 28, 23],
    [12, 1, 18, 27, 0, 13, 6, 11, 3, 8],
    [12, 12, 17, 15, 13, 0, 9, 10, 13, 13],
    [6, 6, 13, 21, 6, 9, 0, 13, 8, 4],
    [19, 10, 25, 25, 11, 10, 13, 0, 9, 17],
    [15, 2, 21, 28, 3, 13, 8, 9, 0, 11],
    [5, 9, 10, 23, 8, 13, 4, 17, 11, 0]
]

weightMatrix =[
    [0, 7, 10, 3, 4, 2, 5, 5, 7, 1],
    [7, 0, 7, 19, 2, 10, 20, 14, 14, 7],
    [10, 7, 0, 20, 16, 5, 13, 3, 9, 4],
    [3, 19, 20, 0, 0, 5, 15, 3, 6, 6],
    [4, 2, 16, 0, 0, 0, 13, 4, 15, 6],
    [2, 10, 5, 5, 0, 0, 0, 8, 7, 2],
    [5, 20, 13, 15, 13, 0, 0, 1, 5, 3],
    [5, 14, 3, 3, 4, 8, 1, 0, 19, 1],
    [7, 14, 9, 6, 15, 7, 5, 19, 0, 20],
    [1, 7, 4, 6, 6, 2, 3, 1, 20, 0],
]

instance = ProblemInstance(n, locations, distanceMatrix, weightMatrix)

selectionMethod = tournamentSelection
crossoverMethod = orderCrossover
mutationMethod = inversion
elitismMethod = pureElitism
populationSize = 500
mutationRate = 0.01
elitismRate = 0.01
generations = 30

# Create and run the genetic algorithm
geneticAlgorithm = GeneticAlgorithm(instance, selectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)

geneticAlgorithmOutput = geneticAlgorithm.run()
geneticAlgorithmSolution = geneticAlgorithmOutput[-1]['min']

# Garantir que o diretório exista
os.makedirs(os.path.dirname('experiments/experiment-0/output.csv'), exist_ok=True)

# Results
applyBruteForce = True # Not recommended for large values of n

# print('\n----------> Problem instance <----------')
# instance.printInstance()
writeProblemInstanceToFile(instance, 'experiments/experiment-0/problem_instance.csv')

# print('\n----------> Output <----------\n')
# printGAOutput(geneticAlgorithmOutput)
writeGAOutputToFile(geneticAlgorithmOutput, 'experiments/experiment-0/output.csv')

# print('\n----------> Solution <----------')

# print(f'\nGenetic algorithm solution:')
# print(geneticAlgorithmSolution)
writeGASolutionToFile(geneticAlgorithmSolution, 'experiments/experiment-0/output.csv')

# if applyBruteForce:
#     bruteForceSolution = (instance.bruteForce())

#     print(f'\nBrute force solution:')
#     print(f'Fitness: {bruteForceSolution[1]}, Permutation: {bruteForceSolution[0]}')
