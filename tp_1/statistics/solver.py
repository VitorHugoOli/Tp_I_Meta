from statistics import mean, pstdev
from typing import List, Callable

from tabulate import tabulate

from matplotlib import pyplot as plt
import pandas as pd

from tp_1.hillClimbling.hill_climbing import hill_climbing
from tp_1.hillClimbling.ils_v2 import ILSearch
from tp_1.hillClimbling.variable import Variable, copyList


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

    def boxplot(self, plot_name=''):
        df = pd.DataFrame({"HS": self.values_hc, "ILS": self.values_ils})
        df.plot.box()
        plt.savefig(plot_name + ".png")


def solver(objective: Callable, variables: List[Variable], repetition: int, plot_name='', basis_limit=None):
    stats = Statistics()
    append_value_hc = stats.values_hc.append
    append_value_ils = stats.values_ils.append

    for i in range(repetition):
        result: List[Variable] = hill_climbing(objective, copyList(variables))
        append_value_hc(objective(*result))

        result: List[Variable] = ILSearch(objective, copyList(variables), basis_limit=basis_limit)
        append_value_ils(objective(*result))

    stats.details()
    stats.boxplot(plot_name)
