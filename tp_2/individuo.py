from typing import List, Callable

import numpy as np

from restrictions import Restriction


class Individuo:
    def __init__(self, dna: np.ndarray):
        self.dna: np.ndarray = np.copy(dna)
        self.eval_value = None

    def __str__(self) -> str:
        return "[" + str(', '.join("{:0.5f}".format(e) for e in self.dna)) + "]"

    @staticmethod
    def penalidade(restriction: Restriction, params: List[float], a=3):
        penalty =  (restriction.alpha * max(0, restriction.restriction(*params))) ** a
        # print(f"Penalidade Aplicada ==> {penalty}")
        return penalty

    def eval(self, objective_function: Callable, restrictions: List[Restriction]):
        if self.eval_value is not None:
            return self.eval_value

        params = list(self.dna)
        
        penalty_sum = sum([self.penalidade(i, params) for i in restrictions]) 
        # print(f'Penalidade aplicada ==> {penalty_sum}')
        self.eval_value = objective_function(*params) + penalty_sum
        
        return self.eval_value
