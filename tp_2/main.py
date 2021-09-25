# (x1 - 10)³ + (x2 - 20)³

from otimizer import Otimizer
from problem2 import get_restrictions, get_variables, objective_2
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
                    elitism_rate= 0.049543083097609256,
                    cut_point=0.7424666860388688,
                    t_individuals=2,
                    n_generations=262, )





def ag_problem_1():
    pop = Population(100, problem_1)

    log.printPop(pop, objective)
    log.printMessage('Antes da selecao')

    while True:
        if pop.generation % 10 == 0:
            log.printPop(pop, objective)

        pop.eval()

        elitists = pop.bourgeois()
        children = pop.surubao()
        pop.x_men(children)

        pop.new_generation((elitists + children))

        if pop.stop_criteria():
            break


problem_2 = Problem(get_variables(),objective_2,get_restrictions(),
                    elitism_rate=0.0667236920820883,
                    cut_point=0.6834153362370213,
                    t_individuals=3,
                    n_generations=175, )

def ag_problem_2():
    pop = Population(100, problem_2)

    log.printPop(pop, objective)
    log.printMessage('Antes da selecao')

    while True:
        if pop.generation % 10 == 0:
            log.printPop(pop, objective)

        pop.eval()

        elitists = pop.bourgeois()
        children = pop.surubao()
        pop.x_men(children)

        pop.new_generation((elitists + children))

        if pop.stop_criteria():
            break


if __name__ == "__main__":
    ot = Otimizer(problem_2)
    ot.get_best_params()
    