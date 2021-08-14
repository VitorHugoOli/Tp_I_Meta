from math import modf
from typing import List
from variable import Variable
from random import random 
import copy

def noise(min, max):
    randomDist = random()
    randomValue = (max - min) * randomDist + min
    return randomDist, randomValue

def initialize(variables:List[Variable]):
    candidates = []
    for variable in variables:
        randomDist, candidateValue = noise(variable.li, variable.ls)
        candidateVariable = Variable(variable.label, variable.li, variable.ls, ri=randomDist ,value=candidateValue)
        candidates.append(candidateVariable)
    return candidates


def modify(candidates:List[Variable], p):
    for candidate in candidates:
        if p >= candidate.ri:
            while True:
                _, candidate.ri = noise(candidate.li, candidate.ls)
                _, n = noise(-candidate.ri, candidate.ri)

                if candidate.li <= (candidate.value + n) <= candidate.ls:
                    break
            candidate.value = candidate.value + n
    return candidates

def quality(candidates:List[Variable], objective):
    # Meno
    q = -objective(candidates)
    print('\nResultado de ' + str(', '.join(str(e) for e in candidates)))
    print(q)
    print( '========\n')
    return q

def isIdeal(candidates:List[Variable]):
    return False


def hill_climbing(variables:List[Variable], objective, p = 1, n_iterations = 30):
    S = initialize(variables)
    MAX_ITERATIONS = 300
    it_count = 0 
    while True:
        it_count = it_count + 1

        R = modify(copy.deepcopy(S), p)
        
        for i in range(n_iterations):
            W = modify(copy.deepcopy(S), p)
            if quality(W,  objective) >= quality(R, objective):
                R = W
        
        if quality(R, objective) > quality(S, objective):
            S = R
        
        if (isIdeal(S) or it_count >= MAX_ITERATIONS):
            print(S)
            break
    return S 