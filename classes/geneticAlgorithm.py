from geneticMethods.selection import *
from geneticMethods.crossover import *
from geneticMethods.mutation import *
from geneticMethods.elitism import *

from classes.problemInstance import ProblemInstance
from classes.individual import Individual
from random import shuffle

# Evaluate the fitness of an individual
def evaluate(permutation, problemInstance):
    fitness = 0

    # Calculate the fitness of the permutation using the distance and weight matrices
    for i in range(problemInstance.size):
        for j in range(i, problemInstance.size):
            fitness += problemInstance.weightMatrix[permutation[i]][permutation[j]] * problemInstance.distanceMatrix[i][j]

    return fitness

# Initialize the population with random permutations
def initializePopulation(populationSize, problemInstance):
    initialPopulation = []

    # Create a list with the available locations, i.e., [0, 1, 2, ..., n-1]
    locations = [i for i in range(0, problemInstance.size)]

    # Create the population with random permutations
    for i in range(0, populationSize):

        # Shuffle the list of available locations, i.e., create a random permutation
        shuffle(locations)
        permutation = locations.copy()

        # Evaluate the fitness of the permutation
        fitness = evaluate(permutation, problemInstance)

        # Create an individual with the permutation and its fitness
        individual = Individual(fitness, permutation)

        # Add the individual to the population
        initialPopulation.append(individual)

    return initialPopulation

# Class that implements an genetic algorithm to the QAP
class GeneticAlgorithm:

    def __init__(self, problemInstance, initialPopulation, selectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations):
        self.problemInstance = problemInstance
        self.initialPopulation = initialPopulation
        self.selectionMethod = selectionMethod
        self.crossoverMethod = crossoverMethod
        self.mutationMethod = mutationMethod
        self.elitismMethod = elitismMethod
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.elitismRate = elitismRate
        self.generations = generations
    
    # Get the population statistics
    def getPopulationStats(self, population):
        minFitness = float('inf')
        maxFitness = float('-inf')
        totalFitness = 0

        for individual in population:
            fitness = individual.fitness
            if fitness < minFitness:
                minFitness = fitness
                minIndividual = individual
            if fitness > maxFitness:
                maxFitness = fitness
                maxIndividual = individual
            totalFitness += fitness

        avgFitness = round(totalFitness / len(population))

        return minIndividual, maxIndividual, avgFitness

    # Evolve the population
    def evolve(self, elite, children):
        newPopulation = []

        # Add the elite individuals to the new population
        for ind in elite:
            newPopulation.append(ind)

        # Add the generated children to the new population
        for child in children:
            newPopulation.append(Individual(evaluate(child, self.problemInstance), child))

        return newPopulation

    def run(self):
        output = []

        actualPopulation = self.initialPopulation

        minIndividual = maxIndividual = avgFitness = None

        for i in range(0, self.generations):
            # Get the population statistics
            minIndividual, maxIndividual, avgFitness = self.getPopulationStats(actualPopulation)

            # Select the elite individuals, they will be preserved for the next generation
            elite = self.elitismMethod(actualPopulation, self.populationSize, self.elitismRate)

            # Select the parents for the crossover
            parents = self.selectionMethod(self.populationSize-len(elite), actualPopulation)

            # Generate the children using the crossover method
            children = self.crossoverMethod(self.populationSize, parents)

            # Mutate the children
            mutatedchildren = self.mutationMethod(children, self.mutationRate)

            # Evolve the population
            actualPopulation = self.evolve(elite, mutatedchildren)

            # Build the output
            generation = {
                'generation': i,
                'min': minIndividual,
                'max': maxIndividual,
                'avg': avgFitness
            }
            output.append(generation)

        return output
