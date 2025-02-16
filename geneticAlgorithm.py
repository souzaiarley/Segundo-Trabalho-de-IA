from instance import Instance
from individual import Individual
from random import shuffle

# Class that implements an genetic algorithm to the QAP
class GeneticAlgorithm:

    def __init__(self, instance):
        self.instance = instance

    # Evaluate the fitness of an individual
    def evaluate(self, permutation):
        fitness = 0

        # Calculate the fitness of the permutation using the distance and weight matrices
        for i in range(self.instance.size):
            for j in range(i, self.instance.size):
                fitness += self.instance.weightMatrix[permutation[i]][permutation[j]] * self.instance.distanceMatrix[i][j]

        return fitness

    # Initialize the population with random permutations
    def initializePopulation(self, populationSize):
        population = []

        # Create a list with the available locations, i.e., [0, 1, 2, ..., n-1]
        locations = [i for i in range(0, self.instance.size)]

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


    def run(self, populationSize):
        # Initialize the population
        population = self.initializePopulation(populationSize)        
