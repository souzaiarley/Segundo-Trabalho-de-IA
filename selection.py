from random import randint

def ranking(populationSize, population):
    # Sort the population by fitness from highest to lowest
    population.sort(key=lambda x: x.fitness, reverse=True)

    for i in population:
        print(i)

    # Create the roulette wheel
    roulette = []

    for i in range(0, populationSize):
        for j in range(i+1):
            roulette.append(i)

    # Select the parents
    parents = []

    for i in range(0, populationSize):
        parent1 = population[roulette[randint(0, len(roulette)-1)]]
        parent2 = population[roulette[randint(0, len(roulette)-1)]]

        parents.append((parent1, parent2))

    return parents
