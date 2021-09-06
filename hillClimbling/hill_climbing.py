from typing import List, Callable
from random import random
import copy

from hillClimbling.aux import noise
from hillClimbling.variable import Variable, copyList

# a(x,y)=-(y+47) sin(sqrt(abs(((x)/(2))+y+47)))-x sin(sqrt(abs(x-(y+47))))
P = 1
HILL_ITERATIONS = 100
HILL_STEEPER_ITERATIONS = 100



def initialize(variables: List[Variable]):
    candidates: List[Variable] = []
    for variable in variables:
        random_dist, candidate_value = noise(variable.li, variable.ls)
        candidate_variable = Variable(variable.label, variable.li, variable.ls, ri=random_dist, value=candidate_value)
        candidates.append(candidate_variable)
    return candidates


def modify(candidates: List[Variable], p):
    # Alterar as margens de buscas(li e ls)
    for candidate in candidates:
        if p >= candidate.ri:  # Não faz senttido
            while True:
                _, candidate.ri = noise(candidate.li, candidate.ls)
                _, n = noise(-candidate.ri, candidate.ri)

                if candidate.li <= (candidate.value + n) <= candidate.ls:
                    break
            candidate.value = candidate.value + n
    return candidates


def quality(candidates: List[Variable], objective):
    q = -objective(*candidates)
    return q


def isIdeal(candidates: List[Variable]):
    pass


def hill_climbing(objective: Callable, variables: List[Variable], p=P, n_iterations=HILL_ITERATIONS, show_result=False):
    s = initialize(variables)
    it_count = 0

    while True:
        it_count += 1

        r = modify(copyList(s), p)

        for i in range(HILL_STEEPER_ITERATIONS):
            w = modify(copyList(s), p)
            if quality(w, objective) >= quality(r, objective):
                r = w

        if quality(r, objective) > quality(s, objective):
            s = r

        if isIdeal(s) or it_count >= n_iterations:
            if show_result:
                print(f"Resultado: ({s[0]},{s[1]}) = {objective(*s)}")
            break

    return s
