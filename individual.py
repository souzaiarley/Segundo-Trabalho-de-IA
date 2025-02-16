# Class that represents an individual in the population
class Individual:
    
    def __init__(self, fitness, permutation):
        self.fitness = fitness
        self.permutation = permutation
        self.permutationString = '-'.join(str(e) for e in permutation)

    def __str__(self):
        return "Fitness: " + str(self.fitness) + ", Permutation: " + self.permutationString
