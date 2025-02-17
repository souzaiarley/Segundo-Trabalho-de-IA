from random import randint

# Function that implements the order crossover(OX) method
def orderCrossover(populationSize, parents):
    offspring = []

    for p in parents:
        # Get the chromosomes of the parents
        chromosome1 = p[0].permutation
        chromosome2 = p[1].permutation

        # Generate two random indices
        i = randint(0, len(chromosome1) - 2)
        j = randint(i + 1, len(chromosome1) - 1)

        # Initialize the children
        fstChild = [-1] * len(chromosome1)
        sndChild = [-1] * len(chromosome1)

        # Copy the selected parts from the parents to the children
        for k in range(i, j + 1):
            fstChild[k] = chromosome1[k]
            sndChild[k] = chromosome2[k]

        # Copy the remaining elements from the second parent to the first child
        for k in range(0, len(chromosome1)):
            if chromosome2[k] not in fstChild:
                for l in range(0, len(chromosome1)):
                    if fstChild[l] == -1:
                        fstChild[l] = chromosome2[k]
                        break

        # Copy the remaining elements from the first parent to the second child
        for k in range(0, len(chromosome1)):
            if chromosome1[k] not in sndChild:
                for l in range(0, len(chromosome1)):
                    if sndChild[l] == -1:
                        sndChild[l] = chromosome1[k]
                        break

        # add the children to the offspring
        offspring.append(fstChild)
        offspring.append(sndChild)

    # Remove the last individual if the offspring size is greater than the population size
    if len(offspring) > populationSize:
        offspring = offspring[:populationSize]

    return offspring

# Function that implements the position-based crossover(PBX) method
def positionBasedCrossover(populationSize, parents):
    offspring = []

    for p in parents:
        # Get the chromosomes of the parents
        chromosome1 = p[0].permutation
        chromosome2 = p[1].permutation

        # Initialize the children
        fstChild = [-1] * len(chromosome1)
        sndChild = [-1] * len(chromosome1)

        # Generate four random indices
        indexes = []

        while len(indexes) < 4:
            index = randint(0, len(chromosome1) - 1)
            if index not in indexes:
                indexes.append(index)

        for index in indexes:
            fstChild[index] = chromosome1[index]
            sndChild[index] = chromosome2[index]

        # Copy the remaining elements from the second parent to the first child
        for k in range(0, len(chromosome1)):
            if chromosome2[k] not in fstChild:
                for l in range(0, len(chromosome1)):
                    if fstChild[l] == -1:
                        fstChild[l] = chromosome2[k]
                        break

        # Copy the remaining elements from the first parent to the second child
        for k in range(0, len(chromosome1)):
            if chromosome1[k] not in sndChild:
                for l in range(0, len(chromosome1)):
                    if sndChild[l] == -1:
                        sndChild[l] = chromosome1[k]
                        break

        # add the children to the offspring
        offspring.append(fstChild)
        offspring.append(sndChild)

    # Remove the last individual if the offspring size is greater than the population size
    if len(offspring) > populationSize:
        offspring = offspring[:populationSize]

    return offspring
