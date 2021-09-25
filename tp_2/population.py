import random
from math import floor
from typing import List, Union

import numpy as np

from individuo import Individuo
from problem import Problem


class Population:
    def __init__(
            self,
            size: int,
            problem: Problem,
    ):
        self.population: List[Individuo] = []
        self.generation = 1
        self.problem = problem
        self.elitists_number = floor(size * self.problem.elitism_rate)
        self.children_number = size - self.elitists_number

        for i in range(size):
            dna = np.full(len(problem.variables), [i.random_value() for i in problem.variables])
            self.population.append(Individuo(dna))

    def eval(self):
        for i in self.population:
            i.eval(self.problem.objective, self.problem.restrictions)

    def bourgeois(self) -> List[Individuo]:
        # Em ordem do pior individuo -> melhor
        if self.elitists_number == 0:
            return []
        sort_population = sorted(self.population, key=lambda x: x.eval_value or 0)
        elitists = sort_population[:self.elitists_number]
        return elitists

    def surubao(self):
        children: List[Individuo] = []
        for i in range(int(self.children_number / 2)):
            parents = [self.lucha_libre() for _ in range(2)]
            children += self.crossing_over(parents)
        return children

    def lucha_libre(self):
        fighters: List[Individuo] = []
        best = random.choice(self.population)
        fighters.append(best)
        for i in range(1, self.problem.t_individuals):
            fighters.append(random.choice(self.population))
            if fighters[i].eval_value < best.eval_value:
                best = fighters[i]
        return best

    def crossing_over(self, parents: List[Individuo]):
        return self.cross_over_simple(parents)

    def cross_over_flat(self, parents):
        brother_dna = np.empty(len(self.problem.variables))
        sister_dna = np.empty(len(self.problem.variables))
        for i in range(len(self.problem.variables)):
            np.append(brother_dna, random.uniform(parents[0].dna[i], parents[1].dna[i]))
            np.append(sister_dna, random.uniform(parents[0].dna[i], parents[1].dna[i]))
        return [Individuo(brother_dna), Individuo(sister_dna)]

    def cross_over_simple(self, parents):
        first_half = floor(len(parents[0].dna) * self.problem.cut_point)
        second_half = -len(parents[0].dna) + first_half
        children: List[Individuo] = []
        for i in range(0, len(parents), 2):
            father_dna = parents[i].dna
            mother_dna = parents[i + 1].dna

            brother_dna = np.concatenate((father_dna[:first_half], mother_dna[second_half:]))
            sister_dna = np.concatenate((mother_dna[:first_half], father_dna[second_half:]))

            children += [Individuo(brother_dna), Individuo(sister_dna)]
        return children

    def new_generation(self, to_add):
        self.generation += 1
        self.population = to_add

    def stop_criteria(self):
        return self.generation == self.problem.n_generations

    def x_men(self, children: List[Individuo]):
        
        if self.problem.mutation_chance > random.random():
            child = random.choice(children)
            child = self.problem.apply_pertubation(child)

    def get_best(self) -> Individuo:
        sort_population = sorted(self.population, key=lambda x: x.eval_value or 0)
        return sort_population[0] 
    
    def solve(self) -> Union[Individuo, float]:
        for i in range(self.problem.n_generations):
            self.eval()
            elitists = self.bourgeois()
            children = self.surubao()
            self.x_men(children)
            self.new_generation((elitists + children))
        best = self.get_best()
        return (best, self.problem.objective(*best.dna))



    def __str__(self) -> str:
        return str(', '.join(str(e) for e in self.population))

    