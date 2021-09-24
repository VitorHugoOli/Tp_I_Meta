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
        parms = list(self.dna)

        ## Penalidade por morte
        
        # for restriction in restrictions:
        #     if not restriction(*parms):
        #         self.eval_value = - np.Infinity
        #         return self.eval_value

        if self.eval_value is not None:
            return self.eval_value


        # Todo: Aplicar metodo de avaliaca das restricoes
        # restricts = [i(*parms) for i in restrictions]

        value = objective_function(*parms)
        self.eval_value = -value
        return self.eval_value

    # Código de corno
    # def rest(self, restrictions:List[Callable]):
    #     parms = list(self.dna)
    #     for index, restriction in enumerate(restrictions):
    #         if not restriction(*parms):
    #             print(f"R{index + 1} ==> Não Satisfeita")
    #         else:
    #             print(f"R{index + 1} ==> Satisfeita")