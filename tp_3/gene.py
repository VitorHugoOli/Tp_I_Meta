from typing_extensions import Literal
from typing import Union

class Gene:
    def __init__(self, name, operator:Literal["<", ">", "=="], value:Union[float, bool], type:Literal["real", "booleano"]):
        self.name = name
        self.value = value
        self.operator = operator
        self.type = type
    def __str__(self) -> str:
        gene_str = ""
        gene_str += "Nome ==>" + str(self.name) + "\n"
        gene_str += "Valor ==> " + str(self.value) + "\n"
        gene_str += "Operador ==> " + str(self.operator) + "\n"
        gene_str += "Tipo ==> " + str(self.type) + "\n"
        return gene_str
