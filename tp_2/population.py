from os import stat_result
from typing import Union, Callable, List
import numpy as np
from individuo import Individuo
from variable import Variable
from math import floor

import random

class Population:
    def __init__(
        self,
        size: int,
        variables: List[Variable],
        restrictions: List[Callable],

        parent_rate:float = 0.2
        cut_point:float = 0.5):

        self.population: List[Individuo] = []
        self.parent_rate = parent_rate
        self.cut_point = cut_point
        self.restrictions = restrictions


        for i in range(size):
            dna = np.full(len(variables), [i.random_value() for i in variables])
            self.population.append(Individuo(dna))

    def __str__(self) -> str:
        return str(', '.join(str(ev ) for e in self.population))

    def eval(self, objective_function: Callable):
        evals = []
        for i in self.population:
            evals.append(i.eval(objective_function, self.restrictions))
        return evals

    def selection(self) -> List[Individuo]:
        
        # Em ordem do pior individuo -> melhor]
        sort_population: np.ndarray = sorted(self.population, key=lambda x: x.eval_value or 0)
        
        parent_cut = floor(len(self.population) * self.parent_rate) 

        parents = sort_population[-parent_cut:]
        worst_ones = sort_population[:parent_cut]

        return parents, worst_ones

    def crossing_over(self, parents:List[Individuo]):
        np.random.shuffle(parents)
        
        first_half = floor(len(parents[0].dna) * self.cut_point) 
        second_half = -len(parents[0].dna) + first_half
        children:List[Individuo] = []

        for i in range(0, len(parents), 2):
            father_dna = parents[i].dna
            mother_dna = parents[i + 1].dna

            brother_dna = np.concatenate((father_dna[:first_half], mother_dna[second_half:]))
            sister_dna = np.concatenate((mother_dna[:first_half], father_dna[second_half:]))

            children += [Individuo(brother_dna), Individuo(sister_dna)]

        return children
    
    def kill_half(self, individuals:List[Individuo]):

        np.random.shuffle(individuals)
        
        choosen_to_kill = individuals[:int(len(individuals)/2)]
        
        for ind in choosen_to_kill:
            if ind in self.population:
                self.population.remove(ind)

    def kill_all(self, individuals:List[Individuo]):
        for ind in individuals:
            if ind in self.population:
                self.population.remove(ind)

    @staticmethod
    def geracional_war(parents:List[Individuo], children:List[Individuo], parent_strength=0.5):
        
        losers = []
        survivors = []
        for i in range(len(parents)):
            parent = parents[i]
            child = children[i]
            
            loser, survivor = (child, parent) if random.random() < parent_strength else (parent, child)
            losers.append(loser)
            survivors.append(survivor)
        
        # Repescagem
        lucky_ones = losers[0::2]
        return survivors, losers, lucky_ones

    def insert(self, individuals:List[Individuo]):
        for individual in individuals:
            if not individual in self.population:
                self.population.append(individual)


    def replace_fellows(self, to_remove, to_add):
        for index, i in enumerate(to_remove):
            self.population = np.where(self.population == i, to_add[index], self.population)


    @staticmethod
    def mutation(children:List[Individuo]):
         
    