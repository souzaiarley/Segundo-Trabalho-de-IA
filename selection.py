from random import randint

# Rank-based selection
def rankingSelection(populationSize, population):
    # Sort the population by cost from highest to lowest
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

# Tournament selection
def executeTournament(population):
    tournament = []
    k = 3

    # Select k individuals randomly from the population
    for i in range(0, k):
        tournament.append(population[randint(0, len(population)-1)])

    # Sort the tournament by cost from lowest to highest
    tournament.sort(key=lambda x: x.fitness)

    # Return the individual with the lowest cost
    return tournament[0]

def tournamentSelection(populationSize, population):
    parents = []

    # Select the parents based on the tournament selection
    for i in range(0, populationSize):
        parent1 = executeTournament(population)
        parent2 = executeTournament(population)

        parents.append((parent1, parent2))

    return parents
