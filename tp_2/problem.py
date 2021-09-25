from random import random
from typing import List, Callable

from restrictions import Restriction
from variable import Variable


class Problem:
    def __init__(
            self,
            variables: List[Variable],
            objective: Callable,
            restrictions: List[Restriction],
            elitism_rate: float = 0.04,
            cut_point: float = 0.5,
            t_individuals: int = 5,
            mutation_chance: float = 0.1,
            n_generations=100
    ):
        """
        @param variables: Variable do Problema
        @param restrictions: Funçoes de restrição do problema
        @param t_individuals: (SELEÇÃO)Numero de individos que entrao no ring
        @param restrictions: (TRATAMENTO DE RESTRIÇÕES) Restriçoes contento a funcao e sua factibilidade
        @param cut_point: (CRUZAMENTO) Ponto de corte no momento do cruzamento
        @param n_generations: (GERACAO) Numero de geracoes
        """
        self.mutation_chance = mutation_chance
        self.n_generations = n_generations
        self.objective = objective
        self.cut_point = cut_point
        self.elitism_rate = elitism_rate
        self.restrictions = restrictions
        self.variables = variables
        self.t_individuals = t_individuals

    def perturbation_vector(self, ohm=1):
        return [(ohm * (i.ls - i.li)) * ((2 * random()) - 1) for i in self.variables]
