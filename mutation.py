from random import randint
from random import random

# Function that implements the exchange mutation (EM)
def exchange(offspring, mutationRate):
    for child in offspring:
        # Check if the mutation will be applied to the child
        if random() < mutationRate:
            # Select two random positions i and j in the permutation
            i = randint(0, len(child) - 1)
            j = randint(0, len(child) - 1)
            while i == j:
                j = randint(0, len(child) - 1)

            # Exchange the elements in positions i and j
            child[i], child[j] = child[j], child[i]

    return offspring

# Function that implements the simple inversion mutation (SIM)
def inversion(offspring, mutationRate):
    for child in offspring:
        # Check if the mutation will be applied to the child
        if random() < mutationRate:
            # Select two random positions i and j in the permutation
            i = randint(0, len(child) - 2)
            j = randint(i + 1, len(child) - 1)

            # Invert the order of the elements between positions i and j
            for k in range(0, (j - i + 1) // 2):
                child[i + k], child[j - k] = child[j - k], child[i + k]

    return offspring
