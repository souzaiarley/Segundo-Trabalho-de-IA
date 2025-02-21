import sys
import os
import time
import csv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from experiments.imports import *

# 1st variation
firstSelectionMethod = tournamentSelection
firstCrossoverMethod = orderCrossover
firstMutationMethod = inversion
firstElitismMethod = pureElitism

# 2nd variation
secondSelectionMethod = tournamentSelection
secondCrossoverMethod = positionBasedCrossover
secondMutationMethod = inversion
secondElitsmMethod = pureElitism

# 3rd variation
thirdSelectionMethod = tournamentSelection
thirdCrossoverMethod = orderCrossover
thirdMutationMethod = inversion
thirdElitismMethod = conditionalElitism

# 4th variation
fourthSelectionMethod = tournamentSelection
fourthCrossoverMethod = orderCrossover
fourthMutationMethod = exchange
fourthElitismMethod = pureElitism

# Genetic algorithm numeric variables
populationSize = 500
mutationRate = 0.01
elitismRate = 0.01
generations = 100

# Clear the CSV file before writing
with open('experiment_5.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Size n', '1st Variation', '2nd Variation', '3rd Variation', '4th Variation'])

# Initial size of the problem instance
n = 10

while True:

    # Create the problem instance
    problemInstance = ProblemInstance(n)
    problemInstance.generateInstance()

    # Create the genetic algorithms
    initialPopulation = initializePopulation(populationSize, problemInstance)

    geneticAlgorithm1 = GeneticAlgorithm(problemInstance, initialPopulation, firstSelectionMethod, firstCrossoverMethod, firstMutationMethod, firstElitismMethod, populationSize, mutationRate, elitismRate, generations)

    geneticAlgorithm2 = GeneticAlgorithm(problemInstance, initialPopulation, secondSelectionMethod, secondCrossoverMethod, secondMutationMethod, secondElitsmMethod, populationSize, mutationRate, elitismRate, generations)

    geneticAlgorithm3 = GeneticAlgorithm(problemInstance, initialPopulation, thirdSelectionMethod, thirdCrossoverMethod, thirdMutationMethod, thirdElitismMethod, populationSize, mutationRate, elitismRate, generations)

    geneticAlgorithm4 = GeneticAlgorithm(problemInstance, initialPopulation, fourthSelectionMethod, fourthCrossoverMethod, fourthMutationMethod, fourthElitismMethod, populationSize, mutationRate, elitismRate, generations)

    # Run the genetic algorithms

    print(f"Running genetic algorithms for problem instance with size = {n}...")

    # Run the genetic algorithms and measure the execution time
    firstStartTime = time.time()
    geneticAlgorithm1.run()
    firstEndTime = time.time()
    executionTime1 = firstEndTime - firstStartTime

    secondStartTime = time.time()
    geneticAlgorithm2.run()
    secondEndTime = time.time()
    executionTime2 = secondEndTime - secondStartTime

    thirdStartTime = time.time()
    geneticAlgorithm3.run()
    thirdEndTime = time.time()
    executionTime3 = thirdEndTime - thirdStartTime

    fourthStartTime = time.time()
    geneticAlgorithm4.run()
    fourthEndTime = time.time()
    executionTime4 = fourthEndTime - fourthStartTime

    times = [executionTime1, executionTime2, executionTime3, executionTime4]

    with open('experiment_5.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([n] + times)

    n += 1
