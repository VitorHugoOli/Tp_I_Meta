from statistics import mean, pstdev
from typing import List, Callable

from tabulate import tabulate

from hillClimbling.hill_climbing import hill_climbing
from hillClimbling.variable import Variable


class Statistics:
    HEAD = ["Algoritmo", "Mínimo", "Máximo", "Média", "Desvio-padrão"]

    def __init__(self):
        self.values_hc = []
        self.values_ils = []

    @staticmethod
    def stats_details(data, algorithm):
        """
        @return min, max, med, std
        """
        if len(data) <= 0:
            return algorithm, 0, 0, 0, 0
        return algorithm, data[0], data[-1], mean(data), pstdev(data)

    def details(self):
        self.values_hc.sort()
        self.values_ils.sort()
        table = [
            self.stats_details(self.values_hc, "HC"),
            self.stats_details(self.values_ils, "ILS"),
        ]
        print(tabulate(table, headers=self.HEAD, tablefmt="fancy_grid"))


def solver(objective: Callable, variables: List[Variable], repetition: int):
    stats = Statistics()
    append_value = stats.values_hc.append
    for i in range(repetition):
        result: List[Variable] = hill_climbing(objective, variables)
        append_value(objective(*result))
    stats.details()
