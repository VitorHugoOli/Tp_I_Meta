from variable import Variable
from population import Population
from typing import Callable
from problem import Problem
import numpy as np
from utils import logger

class Otimizer:

    # Para o Problema 1
    # Melhor fitness de acordo com ILS: -7900

    # Após algumas iterações esse foi o melhor resultado,
    # Vamos explotar até melhorar o fitness

    # cut_point ==> 0.7910958737324651
    # elitism_rate ==> 0.049251111252611265
    # n_generations ==> 275
    # ohm ==> 0.4895654233528705
    # t_individuals ==> 2
    # Indivíduo: ==> [13.02, 0.29]
    # Fitness: ==> -7627.855443184582

    # Após varias mais algumas vezes num contexto mais restrito foi encontrado:

    # cut_point ==> 0.7424666860388688
    # elitism_rate ==> 0.049543083097609256
    # n_generations ==> 262
    # ohm ==> 0.46309697885393863
    # t_individuals ==> 2
    # Indivíduo: ==> [14.26, 0.00]
    # Fitness: ==> -7917.711604230389


    def __init__(self, problem:Problem) -> None:
        self.problem = problem
        self.pop_size = 800
        self.boundaries = [
            Variable("cut_point", 0.2, 0.8),
            Variable("elitism_rate", 0.01, 0.1),
            Variable("n_generations", 100, 1000),
            Variable("ohm", 0.0, 0.1),
            Variable("t_individuals", 2, 6)
        ]

    def get_best_params(self):
        
        while True:
            pop = Population(self.pop_size, self.problem)

            for variable in self.boundaries:
                if type(variable.li) is int:
                    pop.problem.__setattr__(variable.label, np.random.randint(variable.li, variable.ls))
                else:
                    pop.problem.__setattr__(variable.label, np.random.uniform(variable.li, variable.ls))
            
            best, fitness = pop.solve()

            logger.printMessage("Iteração")
            for variable in self.boundaries:
                print(f"{variable.label} ==> {pop.problem.__getattribute__(variable.label)}")
            
            print(f'Indivíduo: ==> {best}')
            print(f'Fitness: ==> {fitness}') 

