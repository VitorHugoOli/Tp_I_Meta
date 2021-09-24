# (x1 - 10)³ + (x2 - 20)³
from math import log
from variable import Variable
from population import Population, Problem, Restriction
from utils import logger as log

count_loop = 0

x1 = Variable('x1', 13, 100)
x2 = Variable('x2', 0, 100)


def objective(x, y):
    return ((x - 10) ** 3) + ((y - 20) ** 3)


def restriction1(x, y):
    return -(x - 5) ** 2 - (y - 5) ** 2 + 100


def restriction2(x, y):
    return (x - 6) ** 2 + (y - 5) ** 2 - 82.81


problem_1 = Problem([x1, x2], objective, [Restriction(restriction1), Restriction(restriction2)])

pop = Population(100, problem_1)

log.printMessage('Antes da selecao')

while True:
    pop.eval()

    parents, worst_ones = pop.selection()

    children = pop.crossing_over(parents)

    pop.kill_half(worst_ones)

    survivors, losers, lucky_ones = Population.geracional_war(parents, children)

    pop.kill_all(losers)
    pop.insert(lucky_ones)
    pop.insert(survivors)

    # Mutacao

    if count_loop % 10 == 0:
        log.printPop(pop, objective)
    count_loop += 1
    if count_loop == 100:
        break
