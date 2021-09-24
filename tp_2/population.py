import random
from math import floor
from typing import List

import numpy as np

from individuo import Individuo
from problem import Problem
from utils.logger import printVector


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

    def bourgeois(self) -> (List[Individuo], List[Individuo]):
        # Em ordem do pior individuo -> melhor
        if self.elitists_number == 0:
            return []
        sort_population = sorted(self.population, key=lambda x: x.eval_value or 0)
        elitists = sort_population[-self.elitists_number:]
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
        np.random.shuffle(parents)

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

    @staticmethod
    def mutation(children: List[Individuo]):
        pass

    def __str__(self) -> str:
        return str(', '.join(str(e) for e in self.population))
