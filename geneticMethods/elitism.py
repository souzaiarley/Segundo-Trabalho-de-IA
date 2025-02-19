from math import ceil

def pureElitism(population, populationSize, eliteRate):
    # Calculate the number of elite individuals
    eliteSize = ceil(populationSize * eliteRate)

    # Sort the population by cost from lowest to highest
    population.sort(key=lambda x: x.fitness)

    # Select the elite individuals
    elite = population[:eliteSize]

    return elite

def conditionalElitism(population, populationSize, eliteRate):
    # Define the diversity limit
    diversityLimit = 0.1

    # Sort the population by cost from lowest to highest
    population.sort(key=lambda x: x.fitness)

    best = population[0]
    worst = population[-1]

    diversityRate = ((worst.fitness*100/best.fitness) - 100)/100

    if diversityRate > diversityLimit:
        # Calculate the number of elite individuals
        eliteSize = ceil(populationSize * eliteRate)

        # Select the elite individuals
        elite = population[:eliteSize]

        return elite

    return []
