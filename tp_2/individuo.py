import random
from typing import List, Callable

import numpy as np



class Individuo:
    def __init__(self, dna: np.ndarray):
        self.dna: np.ndarray = np.copy(dna)
        self.eval_value = None

    def __str__(self) -> str:
        return "[" + str(', '.join(str(e) for e in self.dna)) + "]"

    def eval(self, objective_function: Callable, restrictions: List[Callable]):
        """
        Pontuação do individuo
        @rtype: object
        """

        if self.eval_value is not None:
            return self.eval_value

        parms = list(self.dna)

        # Todo: Aplicar metodo de avaliaca das restricoes
        # restricts = [i(*parms) for i in restrictions]

        value = objective_function(*parms)
        self.eval_value = - value
        return self.eval_value
# f(z) = x + y

# Pop 2 individuos, ex de 1 individuo -->
# [2.2, 3.4]


def stop_criteria(count):
    return count == 300


def suruba(tir) -> np.ndarray:
    mic: np.ndarray = []
    return mic


def mutation(mic):
    og: np.ndarray = []
    return og


def algorithmGenetic(variables, objective_function):
    count = 0

    daonra = Population(10, variables)
    daonra.eval(objective_function)

    while stop_criteria(count):
        tir, naire = daonra.selection()
        mic = suruba(tir)
        og = mutation(mic)

        daonra.replace_fellows(naire, og)

        daonra.eval()
        count += 1
