from hillClimbling.variable import Variable
from typing import List, Callable
from hillClimbling.variable import Variable, copyList

from hillClimbling.hill_climbing import hill_climbing, initialize, modify, noise


P = 1
N_ITERATIONS = 30


def hard_tweak(candidates:List[Variable]):
    for candidate in candidates:
        candidate.value = noise(candidate.li, candidate.ls)
    return candidates

def soft_tweak(candidates:List[Variable]):
    TWEAK_PERCENT_VALUE = 5 / 100
    # | ------------- |
    for candidate in candidates:
        lower_value = TWEAK_PERCENT_VALUE * (candidate.value - candidate.li)
        upper_value = TWEAK_PERCENT_VALUE * (candidate.ls - candidate.value)
        _, candidate.value = noise(lower_value, upper_value)

# Explotação
def better(objective, a, b):
    result_a = objective(*a)
    result_b = objective(*b)
    return a if result_a < result_b else b

# Exploração 
def restart(objective, s1, s2, history):
    return history


def criteria(objective, s1, s2, history):


def ILSearch(objective: Callable, variables: List[Variable], p=P, n_iterations=N_ITERATIONS, show_result=False):
    
    local_search = hill_climbing
    
    #Gerar solução inicial s0
    s0 = initialize(variables)

    #Busca local em s0
    s1 = local_search(objective, s0)

    it_count = 0
    #do
    while True:
        it_count = it_count + 1
    #pertuba
        s2 = modify(s1, 1)
        s3 = local_search(objective, s2)
        s1 = criteria(objective, s2, s3)
    #busca local
        if it_count == 30:
            break
    return s1
    #critério de aceitação
