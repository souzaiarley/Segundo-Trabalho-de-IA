import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from experiments.imports import *

# Problem variables
n = 10

# Create the problem instance
problemInstance = ProblemInstance(n)
problemInstance.generateInstance()

# 1st variation

# Genetic algorithm variables
selectionMethod = tournamentSelection
crossoverMethod = orderCrossover
mutationMethod = inversion
elitismMethod = pureElitism
populationSize = 500
mutationRate = 0.01
elitismRate = 0.01
generations = 30

# 2nd variation

# Genetic algorithm variables
selectionMethod = rankingSelection
crossoverMethod = orderCrossover
mutationMethod = inversion
elitismMethod = pureElitism
populationSize = 500
mutationRate = 0.01
elitismRate = 0.01
generations = 30

# Create the genetic algorithms
geneticAlgorithm1 = GeneticAlgorithm(problemInstance, selectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)
geneticAlgorithm2 = GeneticAlgorithm(problemInstance, selectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)

# Print the problem instance
# print('\n----------> Problem instance <----------')
# problemInstance.printInstance()
writeProblemInstanceToFile(problemInstance, 'experiments/experiment-1/problem_instance.csv')


for i in range(0, 20):
    # print(f'\n----------> Iteration {i} <----------')

    # # Run the genetic algorithms
    # print('\n----------> Running genetic algorithms <----------')

    # print('\n----------> Genetic algorithm 1:')
    geneticAlgorithmOutput1 = geneticAlgorithm1.run()
    # printGAOutput(geneticAlgorithmOutput1)
    writeGAOutputToFile(geneticAlgorithmOutput1, f'experiments/experiment-1/outputs/output{i}.csv')

    # print('\n----------> Genetic algorithm 2:')
    geneticAlgorithmOutput2 = geneticAlgorithm2.run()
    # printGAOutput(geneticAlgorithmOutput2)
    writeGAOutputToFile(geneticAlgorithmOutput2, f'experiments/experiment-1/outputs/output{i}.csv')

    # Results
    # print('\n----------> Solutions <----------')

    geneticAlgorithmSolution1 = geneticAlgorithmOutput1[-1]['min']
    geneticAlgorithmSolution2 = geneticAlgorithmOutput2[-1]['min']

    # print(f'\nGenetic algorithm solution 1:')
    # print(geneticAlgorithmSolution1)
    # print(f'\nGenetic algorithm solution 2:')
    # print(geneticAlgorithmSolution2)

