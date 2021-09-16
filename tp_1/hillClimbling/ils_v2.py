import random

from hillClimbling.variable import Variable
from typing import List, Callable
from hillClimbling.variable import Variable, copyList
from hillClimbling.hill_climbing import hill_climbing, initialize, modify, noise
import numpy as np

N_ITERATIONS = 100
BASIS_LIMIT = 30


class MemoryILS:
    def __init__(self, basis_limit=BASIS_LIMIT):
        self.basis_limit = basis_limit
        self.history = []
        self.best_variables: List[Variable] = []
        self.iterations: int = 0

    def increaseIteration(self):
        self.iterations += 1

    def terminated(self):
        return self.iterations >= N_ITERATIONS

    def isInSameBasis(self, value):
        """
        Verifica para o valor passado se este está em um raio de self.basis_limit em relaçõo aos valores da memoria
        """
        for i in self.history:
            if i + self.basis_limit <= value <= i - self.basis_limit:
                return True
        return False

    def isWorstThanAllMemory(self, value):
        """
        Verifica para o valor passado se este este é pior que os demais valores da memoria
        :@return
            True = pior que a memoria
            False = melhor que a memoria
        """
        self.history.sort()
        return False if len(self.history) == 0 else (value > self.history[-1])

    def acceptanceProbability(self):
        return (N_ITERATIONS - self.iterations) / N_ITERATIONS


def perturbation(objective, s: List[Variable], memory: MemoryILS):
    """
    Calcula um pertubacao atual para variaveis de decisão e valida se o valor
    objetivo das variaveis de decisão esta distante em um raio de BASIS_LIMIT dos
    valores armazenados no history
    """
    while True:
        for i in s:
            i.value = (i.ls - i.li) * random.random() + i.li

        if not memory.isInSameBasis(objective(*s)):
            memory.history.append(objective(*s))
            return s


def criteria(objective, s_old: List[Variable], s_new: List[Variable], memory: MemoryILS):
    """
    @param objective:
    @param s_old: Varaiveis de decisão antigo
    @param s_new: Varaiveis de decisão apos pertubação e busca local
    @param memory:
    """

    value_s_new = objective(*s_new)

    # Se for melhor que todos aramazena em memoria
    if objective(*memory.best_variables) > value_s_new:
        memory.best_variables = s_new
        return s_new  # Explotar

    # Se for pior que todos na memoria e for pior que o valor objetivo de s1
    if memory.isWorstThanAllMemory(value_s_new) and value_s_new > objective(*s_old):
        if memory.acceptanceProbability() > random.random():
            return s_new
        else:
            return s_old
    else:
        return s_old


def ILSearch(objective: Callable, variables: List[Variable], local_search=None, basis_limit=BASIS_LIMIT):
    memory = MemoryILS(basis_limit)
    local_search = local_search or hill_climbing

    s0 = initialize(variables)  # Gerar solução inicial s0
    s1 = local_search(objective, s0, n_iterations=100)  # Busca local em s0
    memory.best_variables = s1

    while True:
        memory.increaseIteration()

        s2 = perturbation(objective, copyList(s1), memory)
        s3 = local_search(objective, s2, n_iterations=100)
        s1 = criteria(objective, s1, s3, memory)

        if memory.terminated():
            break

    return s1
