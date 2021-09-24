from collections import Callable


class Restriction:
    def __init__(self, restriction: Callable, alpha=0.4):
        """

        @param restriction: (TRATAMENTO DE RESTRIÇÕES) Funcao da restrição
        @param alpha: (TRATAMENTO DE RESTRIÇÕES) Factibilidade de aceitação de uma restrição
        """
        self.restriction = restriction
        self.alpha = alpha
