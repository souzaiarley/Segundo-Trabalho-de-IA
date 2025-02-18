from math import ceil

def elitism(population, populationSize, eliteRate):
    # Calculate the number of elite individuals
    eliteSize = ceil(populationSize * eliteRate)

    # Sort the population by cost from lowest to highest
    population.sort(key=lambda x: x.fitness, reverse=True)

    # Select the elite individuals
    elite = population[:eliteSize]

    return elite