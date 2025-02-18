import geneticMethods.selection as selection
import geneticMethods.crossover as crossover
import geneticMethods.mutation as mutation
import geneticMethods.elitism as elitism

from problemInstance import ProblemInstance
from individual import Individual
from random import shuffle

# Class that implements an genetic algorithm to the QAP
class GeneticAlgorithm:

    def __init__(self, problemInstance, selectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations):
        self.problemInstance = problemInstance
        self.selectionMethod = selectionMethod
        self.crossoverMethod = crossoverMethod
        self.mutationMethod = mutationMethod
        self.elitismMethod = elitismMethod
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.elitismRate = elitismRate
        self.generations = generations

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
            permutation = locations.copy()

            # Evaluate the fitness of the permutation
            fitness = self.evaluate(permutation)

            # Create an individual with the permutation and its fitness
            individual = Individual(fitness, permutation)

            # Add the individual to the population
            population.append(individual)

        return population
    
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
            newPopulation.append(Individual(self.evaluate(child), child))

        return newPopulation

    def run(self):
        # Generate the initial population randomly
        population = self.initializePopulation(self.populationSize)

        minIndividual = maxIndividual = avgFitness = None

        for i in range(0, self.generations):
            print(f'\nGeneration {i}')

            # Get the population statistics
            minIndividual, maxIndividual, avgFitness = self.getPopulationStats(population)

            print(f'Individual with lowest cost: {minIndividual}')
            print(f'Individual with highest cost: {maxIndividual}')
            print(f'Average cost: {avgFitness}')

            # Select the elite individuals, they will be preserved for the next generation
            elite = self.elitismMethod(population, self.populationSize, self.elitismRate)

            # Select the parents for the crossover
            parents = self.selectionMethod(self.populationSize-len(elite), population)

            # Generate the children using the crossover method
            children = self.crossoverMethod(self.populationSize, parents)

            # Mutate the children
            mutatedchildren = self.mutationMethod(children, self.mutationRate)

            # Evolve the population
            population = self.evolve(elite, mutatedchildren)

        return minIndividual
