# (x1 - 10)³ + (x2 - 20)³

from population import Problem, Population
from restrictions import Restriction
from utils import logger as log
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
                    elitism_rate=0.002,
                    cut_point=0.5,
                    t_individuals=3,
                    n_generations=100, )

pop = Population(1000, problem_1)

log.printPop(pop, objective)

log.printMessage('Antes da selecao')

while True:
    if pop.generation % 10 == 0:
        log.printPop(pop, objective)

    pop.eval()

    elitists = pop.bourgeois()
    children = pop.surubao()

    # Mutacao

    pop.new_generation((elitists + children))

    if pop.stop_criteria():
        break
