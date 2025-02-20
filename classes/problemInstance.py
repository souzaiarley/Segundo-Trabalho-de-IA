import math
from random import randint

# Function that calculates the Euclidean distance between two points
def euclidean(fstlocation, sndlocation) -> float:
    x1, y1 = fstlocation[0], fstlocation[1]
    x2, y2 = sndlocation[0], sndlocation[1]
    return math.floor(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


# Class that represents an instance of the QA problem
class ProblemInstance:
    
    def __init__(self, n, locations=[], distanceMatrix=[], weightMatrix=[]):
        self.size = n
        self.locations = locations
        self.distanceMatrix = distanceMatrix
        self.weightMatrix = weightMatrix

    # Function that generates the coordinates of the locations
    def generatelocations(self, n):
        locations = []

        for i in range(n):
            locations.append((randint(0, 30), randint(0, 30)))

        self.locations = locations

    # Function that generates the distance matrix
    def generateDistanceMatrix(self, n):
        distanceMatrix = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(i, n):
                distanceMatrix[i][j] = euclidean(self.locations[i], self.locations[j])
                distanceMatrix[j][i] = distanceMatrix[i][j]

        self.distanceMatrix = distanceMatrix

    # Function that generates the weight matrix
    def generateWeightMatrix(self, n):
        weightMatrix = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    weightMatrix[i][j] = 0
                    weightMatrix[j][i] = 0
                else:
                    weightMatrix[i][j] = randint(0, 2*n)
                    weightMatrix[j][i] = weightMatrix[i][j]

        self.weightMatrix = weightMatrix

    # Function that generates the instance randomly
    def generateInstance(self):
        self.generatelocations(self.size)
        self.generateDistanceMatrix(self.size)
        self.generateWeightMatrix(self.size)

    # Function that prints the instance
    def printInstance(self):
        print("Locations: ", self.locations)
        
        print("\nDistance Matrix: ")
        for line in self.distanceMatrix:
            print(line)

        print("\nWeight Matrix: ")
        for line in self.weightMatrix:
            print(line)
