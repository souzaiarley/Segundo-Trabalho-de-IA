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
firstSelectionMethod = tournamentSelection

# 2nd variation
secondSelectionMethod = rankingSelection

# Genetic algorithm variables
crossoverMethod = orderCrossover
mutationMethod = inversion
elitismMethod = pureElitism
populationSize = 500
mutationRate = 0.01
elitismRate = 0.01
generations = 100

# Create the genetic algorithms
initialPopulation = initializePopulation(populationSize, problemInstance)

geneticAlgorithm1 = GeneticAlgorithm(problemInstance, initialPopulation, firstSelectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)
geneticAlgorithm2 = GeneticAlgorithm(problemInstance, initialPopulation, secondSelectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)

os.makedirs(os.path.dirname('experiments/experiment-1/problem_instance.csv'), exist_ok=True)
writeProblemInstanceToFile(problemInstance, 'experiments/experiment-1/problem_instance.csv')

# Garante que o diretório existe
os.makedirs(os.path.dirname('experiments/experiment-1/outputs/'), exist_ok=True)

for i in range(0, 20):
    geneticAlgorithmOutput1 = geneticAlgorithm1.run()
    writeGAOutputToFile(geneticAlgorithmOutput1, f'experiments/experiment-1/outputs/{i}_firstAlgorithm.csv')

    geneticAlgorithmOutput2 = geneticAlgorithm2.run()
    writeGAOutputToFile(geneticAlgorithmOutput2, f'experiments/experiment-1/outputs/{i}_secondAlgorithm.csv')

    geneticAlgorithmSolution1 = geneticAlgorithmOutput1[-1]['min']
    geneticAlgorithmSolution2 = geneticAlgorithmOutput2[-1]['min']
