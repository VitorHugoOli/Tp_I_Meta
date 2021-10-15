from statistics import mean, pstdev

from tabulate import tabulate

from population import Population


class Statistics:
    HEAD = ["Algoritmo", "Mínimo", "Máximo", "Média", "Desvio-padrão"]

    def __init__(self):
        self.values_ag = []

    @staticmethod
    def stats_details(data, algorithm):
        """
        @return min, max, med, std
        """
        if len(data) <= 0:
            return algorithm, 0, 0, 0, 0
        return algorithm, data[0], data[-1], mean(data), pstdev(data)

    def details(self):
        self.values_ag.sort()
        table = [
            self.stats_details(self.values_ag, "AG"),
        ]
        print(tabulate(table, headers=self.HEAD, tablefmt="fancy_grid"))


def solver(problem, n_individuals, repetition: int):
    stats = Statistics()
    append_value_ag = stats.values_ag.append

    for i in range(repetition):
        pop = Population(n_individuals, problem)
        append_value_ag(pop.solve()[1])

    stats.details()
