import random


class Variable:
    def __init__(self, label, li, ls):
        self.label = label
        self.li = li  # Limit inferior
        self.ls = ls  # Limit superior

    def random_value(self):
        return random.uniform(self.li, self.ls)
