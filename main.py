import os
import ast

from classes.problemInstance import *
from classes.geneticAlgorithm import *
from experiments.output import *

# Problem variables
print('\n----------> Size of N <----------\n')
n = int(input('Enter N value: '))

os.system('cls')
os.system('clear')

# Create the problem instance
problemInstance = ProblemInstance(n)

print('\n----------> Instance <----------\n')
print('[1] Random instance')
print('[2] Custom instance')
instanceType = int(input('\nEnter the instance type: '))

os.system('cls')
os.system('clear')

if instanceType != 1 and instanceType != 2:
    raise ValueError('Invalid instance type')

if instanceType == 1:
    problemInstance.generateInstance()
else:
    with open('customInstance.txt', 'r') as f:
        content = f.read().strip()

    lists = content.split('\n\n')

    locations = ast.literal_eval(lists[0])
    weightMatrix = ast.literal_eval(lists[1])

    if len(locations) != n:
        raise ValueError('Invalid number of locations')
    
    if len(weightMatrix) != n:
        raise ValueError('Invalid weight matrix')
    
    for i in range(n):
        if len(weightMatrix[i]) != n:
            raise ValueError('Invalid weight matrix')

    problemInstance.locations = locations
    problemInstance.generateDistanceMatrix(n)
    problemInstance.weightMatrix = weightMatrix

# Genetic algorithm variables
selectionMethod = None
crossoverMethod = None
mutationMethod = None
elitismMethod  = None
populationSize = None
mutationRate = None
elitismRate = None
generations = None

print('\n----------> Selection Method <----------\n')
print('[1] Tournament selection')
print('[2] Ranking selection')
selectionMethod = int(input('\nEnter the selection method: '))

os.system('cls')
os.system('clear')

if selectionMethod != 1 and selectionMethod != 2:
    raise ValueError('Invalid selection method')

if selectionMethod == 1:
    selectionMethod = tournamentSelection
else:
    selectionMethod = rankingSelection

print('\n----------> Crossover Method <----------\n')
print('[1] Order crossover')
print('[2] Position-based crossover')
crossoverMethod = int(input('\nEnter the crossover method: '))

os.system('cls')
os.system('clear')

if crossoverMethod != 1 and crossoverMethod != 2:
    raise ValueError('Invalid crossover method')

if crossoverMethod == 1:
    crossoverMethod = orderCrossover
else:
    crossoverMethod = positionBasedCrossover

print('\n----------> Mutation Method <----------\n')
print('[1] Exchange mutation')
print('[2] Inversion mutation')
mutationMethod = int(input('\nEnter the mutation method: '))

os.system('cls')
os.system('clear')

if mutationMethod != 1 and mutationMethod != 2:
    raise ValueError('Invalid mutation method')

if mutationMethod == 1:
    mutationMethod = exchange
else:
    mutationMethod = inversion

print('\n----------> Elitism Method <----------\n')
print('[1] Pure elitism')
print('[2] Conditional elitism')
elitismMethod = int(input('\nEnter the elitism method: '))

os.system('cls')
os.system('clear')

if elitismMethod != 1 and elitismMethod != 2:
    raise ValueError('Invalid elitism method')

if elitismMethod == 1:
    elitismMethod = pureElitism
else:
    elitismMethod = conditionalElitism

print('\n----------> Numeric Variables <----------\n')
populationSize = int(input('Enter the population size: '))
generations = int(input('Enter the number of generations: '))
mutationRate = float(input('Enter the mutation rate: '))
elitismRate = float(input('Enter the elitism rate: '))

# Create and run the genetic algorithm
geneticAlgorithm = GeneticAlgorithm(problemInstance, selectionMethod, crossoverMethod, mutationMethod, elitismMethod, populationSize, mutationRate, elitismRate, generations)

geneticAlgorithmOutput = geneticAlgorithm.run()
geneticAlgorithmSolution = geneticAlgorithmOutput[-1]['min']

print('\n----------> Output <----------\n')
printGAOutput(geneticAlgorithmOutput)

print('\n----------> Solution <----------')

print(f'\nGenetic algorithm solution:')
print(geneticAlgorithmSolution)
