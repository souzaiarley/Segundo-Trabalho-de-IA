import selection as selection
import crossover as crossover
import mutation as mutation
import elitism as elitism

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
        min_fitness = float('inf')
        max_fitness = float('-inf')
        total_fitness = 0

        for individual in population:
            fitness = individual.fitness
            if fitness < min_fitness:
                min_fitness = fitness
                min_individual = individual
            if fitness > max_fitness:
                max_fitness = fitness
                max_individual = individual
            total_fitness += fitness

        avg_fitness = round(total_fitness / len(population))

        return min_individual, max_individual, avg_fitness

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

        for i in range(0, self.generations):
            print(f'Generation {i}')

            # Get the population statistics
            min_individual, max_individual, avg_fitness = self.getPopulationStats(population)

            print(f'Individual with lowest cost: {min_individual.fitness}')
            print(f'Individual with highest cost: {max_individual.fitness}')
            print(f'Average cost: {avg_fitness}')

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

            print()


if __name__ == '__main__':
    # Problem variables
    n = 10

    # Create the problem instance
    problemInstance = ProblemInstance(n)
    problemInstance.generateInstance()

    # Genetic algorithm variables
    selectionMethod = selection.tournamentSelection
    crossoverMethod = crossover.orderCrossover
    mutationMethod = mutation.exchange
    elitismMethod = elitism.elitism
    populationSize = 30
    mutationRate = 0.1
    elitismRate = 0.05
    generations = 100

    # Create and run the genetic algorithm
    geneticAlgorithm = GeneticAlgorithm(problemInstance, selectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)

    geneticAlgorithm.run()
