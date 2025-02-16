import selection

from problemInstance import ProblemInstance
from individual import Individual
from random import shuffle

# Class that implements an genetic algorithm to the QAP
class GeneticAlgorithm:

    def __init__(self, problemInstance, selectionMethod, populationSize):
        self.problemInstance = problemInstance
        self.selectionMethod = selectionMethod
        self.populationSize = populationSize

    # Evaluate the fitness of an individual
    def evaluate(self, permutation):
        fitness = 0

        # Calculate the fitness of the permutation using the distance and weight matrices
        for i in range(self.problemInstance.size):
            for j in range(i, self.problemInstance.size):
                fitness += self.problemInstance.weightMatrix[permutation[i]][permutation[j]] * self.problemInstance.distanceMatrix[i][j]

        return fitness

    # Initialize the population with random permutations
    def initializePopulation(self, populationSize):
        population = []

        # Create a list with the available locations, i.e., [0, 1, 2, ..., n-1]
        locations = [i for i in range(0, self.problemInstance.size)]

        # Create the population with random permutations
        for i in range(0, populationSize):

            # Shuffle the list of available locations, i.e., create a random permutation
            shuffle(locations)
            permutation = locations

            # Evaluate the fitness of the permutation
            fitness = self.evaluate(permutation)

            # Create an individual with the permutation and its fitness
            individual = Individual(fitness, permutation)

            # Add the individual to the population
            population.append(individual)

        return population


    def run(self):
        # Initialize the population
        population = self.initializePopulation(self.populationSize)

        parents = self.selectionMethod(self.populationSize, population)

