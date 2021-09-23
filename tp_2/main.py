# (x1 - 10)³ + (x2 - 20)³
from math import log
from variable import Variable
from population import Population
from utils import logger

x1 = Variable('x1', 13, 100)
x2 = Variable('x2', 0, 100)

def problem(x1, x2):
    return ((x1 - 10) ** 3) + ((x2 - 20) ** 3)

pop = Population(100, [x1, x2])

logger.printMessage('Antes da selecao')
# logger.logPop(pop, problem)

for i in range(100):
    parents, worst_ones = pop.selection()
    children = pop.crossing_over(parents)
    pop.kill_half(worst_ones)
    
    survivors, losers, lucky_ones = Population.geracional_war(parents, children)
    
    pop.kill_all(losers)
    pop.insert(lucky_ones)
    pop.insert(survivors)
    if i % 10 == 0:
        logger.logPop(pop, problem)

logger.printMessage('Depois da seleção')
# logger.logPop(pop, problem)


