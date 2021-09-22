from typing import Union, Callable, List
import numpy as np
from individuo import Individuo
from variable import Variable
from math import floor

class Population:
    def __init__(
        self,
        size: int,
        variables: List[Variable],
        parent_rate:float = 0.2,
        cut_point:float = 0.5):

        self.population: List[Individuo] = []
        self.parent_rate = parent_rate
        self.cut_point = cut_point

        for i in range(size):
            dna = np.full(len(variables), [i.random_value() for i in variables])
            self.population.append(Individuo(dna))

    def __str__(self) -> str:
        return str(', '.join(str(e) for e in self.population))

    def eval(self, objective_function: Callable, restrictions: List[Callable]):
        evals = []
        for i in self.population:
            evals.append(i.eval(objective_function, restrictions))
        return evals

    def selection(self) -> List[Individuo]:

        # Em ordem do pior individuo -> melhor 
        sort_population: np.ndarray = sorted(self.population, key=lambda x: x.eval_value or 0)
        parents = sort_population[floor(-len(self.population) * self.parent_rate):]
        
        return parents

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
    
    # def survivor():


    def best_fellow(self):
        return self.population.sort()[0]

    def replace_fellows(self, to_remove, to_add):
        for index, i in enumerate(to_remove):
            self.population = np.where(self.population == i, to_add[index], self.population)