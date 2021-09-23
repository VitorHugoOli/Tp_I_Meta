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
        self.eval_value = -value
        return self.eval_value