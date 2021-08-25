from typing import List, Callable
from random import random
import copy

from hillClimbling.variable import Variable, copyList

P = 1
N_ITERATIONS = 30


def initialize(variables: List[Variable]):
    candidates = []
    for variable in variables:
        random_dist, candidate_value = noise(variable.li, variable.ls)
        candidate_variable = Variable(variable.label, variable.li, variable.ls, ri=random_dist, value=candidate_value)
        candidates.append(candidate_variable)
    return candidates


def noise(min_value, max_value):
    random_dist = random()
    random_value = (max_value - min_value) * random_dist + min_value
    return random_dist, random_value


def modify(candidates: List[Variable], p):
    for candidate in candidates:
        if p >= candidate.ri:
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


def hill_climbing(objective: Callable, variables: List[Variable], p=P, n_iterations=N_ITERATIONS, show_result=False):
    s = initialize(variables)
    max_iterations = 300
    it_count = 0
    while True:
        it_count += 1

        r = modify(copyList(s), p)

        for i in range(n_iterations):
            w = modify(copyList(s), p)
            if quality(w, objective) >= quality(r, objective):
                r = w

        if quality(r, objective) > quality(s, objective):
            s = r

        if isIdeal(s) or it_count >= max_iterations:
            if show_result:
                print(f"Resultado: ({s[0]},{s[1]}) = {objective(*s)}")
            break

    return s
