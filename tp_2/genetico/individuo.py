import random
from typing import List, Callable

import numpy as np


class Variable:
    def __init__(self, label, li, ls):
        self.label = label
        self.li = li  # Limit inferior
        self.ls = ls  # Limit superior

    def random_value(self):
        return random.randrange(self.li, self.ls)


class Gene:
    def __init__(self, value, restriction, var: Variable):
        self.restriction = restriction
        self.var = var
        self.value = value


class Individuo:
    def __init__(self, dna: np.ndarray):
        self.dna: np.ndarray = np.copy(dna)
        self.eval_value = None

    def eval(self, objective_function: Callable, restrictions: List[Callable]):
        """
        Pontuação do individuo
        @rtype: object
        """
        if self.eval_value is not None:
            return self.eval_value

        parms = list(self.dna)
        # Todo: Aplicar metodo de avaliaca das restricoes
        restricts = [i(*parms) for i in restrictions]

        value = objective_function(*parms)
        self.eval_value = value - sum(restricts)
        return self.eval_value


class Population:
    def __init__(self, size: int, variables: List[Variable]):
        self.population: np.ndarray = np.empty(len(variables))
        for i in range(size):
            dna = np.full(len(variables), [i.random_value() for i in variables])
            self.population[i] = Individuo(dna)

    def eval(self, objective_function: Callable, restrictions: List[Callable]):
        """
        Avaliação fitness
        @rtype: object
        """
        for i in self.population:
            i.eval(objective_function, restrictions)

    def selection(self) -> (np.ndarray, np.ndarray):
        """
        Selecionar 2 pais
        Selecionar 2 piores
        """
        sort_population: np.ndarray = self.population.sort()
        return sort_population[:1], sort_population[-1:-2]

    def best_fellow(self):
        return self.population.sort()[0]

    def replace_fellows(self, to_remove, to_add):
        for index, i in enumerate(to_remove):
            self.population = np.where(self.population == i, to_add[index], self.population)


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
