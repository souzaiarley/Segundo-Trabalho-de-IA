from math import ceil

def pureElitism(population, populationSize, eliteRate):
    # Calculate the number of elite individuals
    eliteSize = ceil(populationSize * eliteRate)

    # Sort the population by cost from lowest to highest
    population.sort(key=lambda x: x.fitness)

    # Select the elite individuals
    elite = population[:eliteSize]

    return elite

def balancedElitism(population, populationSize, eliteRate):
    # Calculate the number of elite individuals
    eliteSize = ceil(populationSize * eliteRate)

    # Sort the population by cost from lowest to highest
    population.sort(key=lambda x: x.fitness)

    # Select the elite individuals
    elite = population[:eliteSize]

    # Select the worst individuals
    elite = elite[::-1]
    worstElite = elite[:eliteSize//2]
    return worstElite
