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
firstCrossoverMethod = orderCrossover

# 2nd variation
secondCrossoverMethod = positionBasedCrossover

# Genetic algorithm variables
selectionMethod = tournamentSelection
mutationMethod = inversion
elitismMethod = pureElitism
populationSize = 500
mutationRate = 0.01
elitismRate = 0.01
generations = 100

# Create the genetic algorithms
initialPopulation = initializePopulation(populationSize, problemInstance)

geneticAlgorithm1 = GeneticAlgorithm(problemInstance, initialPopulation, selectionMethod, firstCrossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)
geneticAlgorithm2 = GeneticAlgorithm(problemInstance, initialPopulation, selectionMethod, secondCrossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)

os.makedirs(os.path.dirname('experiments/experiment-2/problem_instance.csv'), exist_ok=True)
writeProblemInstanceToFile(problemInstance, 'experiments/experiment-2/problem_instance.csv')

# Garantir que o diretório exista
os.makedirs(os.path.dirname('experiments/experiment-2/outputs/'), exist_ok=True)

for i in range(0, 20):
    geneticAlgorithmOutput1 = geneticAlgorithm1.run()
    writeGAOutputToFile(geneticAlgorithmOutput1, f'experiments/experiment-2/outputs/{i}_firstAlgorithm.csv')

    geneticAlgorithmOutput2 = geneticAlgorithm2.run()
    writeGAOutputToFile(geneticAlgorithmOutput2, f'experiments/experiment-2/outputs/{i}_secondAlgorithm.csv')

    geneticAlgorithmSolution1 = geneticAlgorithmOutput1[-1]['min']
    geneticAlgorithmSolution2 = geneticAlgorithmOutput2[-1]['min']
