import random
from typing import List


class Attribute:
    def __init__(self, name: str, possible_op_comp: List, range_value: List):
        self.range_value = range_value
        self.possible_op_comp = possible_op_comp
        self.name = name

    def mutation(self):
        pass


class BoolAttribute(Attribute):
    def __init__(self, name: str):
        super().__init__(name, ["==", "!="], [True, False])

    def mutation(self) -> (str, bool):
        return random.choice(self.possible_op_comp), random.choice(self.range_value)


class MultiAttribute(Attribute):
    def __init__(self, name: str, range_value: List):
        super().__init__(name, ["==", "!="], range_value)

    def mutation(self) -> (str, bool):
        return random.choice(self.possible_op_comp), random.choice(self.range_value)


class RealAttribute(Attribute):
    def __init__(self, name: str, range_value: List):
        super().__init__(name, [">=", "<="], range_value)

    def mutation(self) -> (str, bool):
        return random.choice(self.possible_op_comp), random.choice(self.range_value)


class LogicAttribute(Attribute):
    def __init__(self):
        super().__init__("Logic_Op", [], ["and", "or"])

    def mutation(self) -> str:
        return random.choice(self.range_value)


class Gene:
    def __init__(self, attr: Attribute):
        self.attr = attr
        if attr is not LogicAttribute:
            value, op_comp = attr.mutation()
            self.value = value
            self.op_comp = op_comp
        else:
            self.value = attr.mutation()
            self.op_comp = "-"

    def __str__(self) -> str:
        # Gene do tipo experessão: self.attr.nome self.op_comp self.value
        # Gene do tipo op_logic: self.value
        gene_str = ""
        gene_str += "Nome ==>" + str(self.attr.name) + "\n"
        gene_str += "Valor ==> " + str(self.value) + "\n"
        gene_str += "Op_comp ==> " + str(self.op_comp) + "\n"
        gene_str += "Tipo ==> " + str(type(self.attr)) + "\n"
        return gene_str
