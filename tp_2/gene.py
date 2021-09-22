class Gene:
    def __init__(self, value, restriction, var: Variable):
        self.restriction = restriction
        self.var = var
        self.value = value