# (x1 - 10)³ + (x2 - 20)³
from math import log
from variable import Variable
from population import Population
from utils import logger


count_loop = 0 

x1 = Variable('x1', 13, 100)
x2 = Variable('x2', 0, 100)

def problem(x1, x2):
    return ((x1 - 10) ** 3) + ((x2 - 20) ** 3)

def restriction1(x1,x2):
    return (-((x1 - 5) ** 2) - ((x2 - 5) ** 2) + 100) <= 0 

def restriction2(x1, x2):
    return (((x1 - 6) ** 2) + ((x2 - 5) ** 2) - 82.81) <= 0


pop = Population(100, [x1, x2], restrictions=[restriction1, restriction2])




logger.printMessage('Antes da selecao')
# logger.logPop(pop, problem)



print(restriction1(15,12))
print(restriction2(10,12))

while True:
    pop.eval(problem)
    parents, worst_ones = pop.selection()

    children = pop.crossing_over(parents)
    
    pop.kill_half(worst_ones)
    
    survivors, losers, lucky_ones = Population.geracional_war(parents, children)
    
    pop.kill_all(losers)
    pop.insert(lucky_ones)
    pop.insert(survivors)


    # Mutacao


    if count_loop % 10 == 0:
        logger.logPop(pop, problem)    
    count_loop += 1
    if count_loop == 100:
        break


