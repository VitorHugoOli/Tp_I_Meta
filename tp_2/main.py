# (x1 - 10)³ + (x2 - 20)³

from population import Problem
from problem2 import get_variables, objective_2, get_restrictions
from restrictions import Restriction
from statistics_s.solver import solver
from utils.logger import printMessage
from variable import Variable

count_loop = 0

x1 = Variable('x1', 13, 100)
x2 = Variable('x2', 0, 100)


def objective(x, y):
    return ((x - 10) ** 3) + ((y - 20) ** 3)


def restriction1(x, y):
    return -(x - 5) ** 2 - (y - 5) ** 2 + 100


def restriction2(x, y):
    return (x - 6) ** 2 + (y - 5) ** 2 - 82.81


problem_1 = Problem([x1, x2], objective,
                    [Restriction(restriction1), Restriction(restriction2)],
                    elitism_rate=0.049543083097609256,
                    cut_point=0.7424666860388688,
                    t_individuals=2,
                    n_generations=262, )

problem_2 = Problem(get_variables(), objective_2, get_restrictions(),
                    elitism_rate=0.0667236920820883,
                    cut_point=0.6834153362370213,
                    t_individuals=3,
                    n_generations=175, )

if __name__ == "__main__":
    printMessage("Problema 1")
    solver(problem_1, 400, 30)
    printMessage("Problema 2")
    solver(problem_2, 400, 30)
