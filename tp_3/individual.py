from gene import Gene
from typing import List
from pandas import read_csv
from random import choice, random

class Individuo:
    TABLE = read_csv("clean_table.csv")
    NUMBER_RULES = 19
    
    def __init__(self):
        
        dna = []
        real_columns = ["mesescomocliente", "valormensal", "totalgasto"]
        select_columns = []
        
        for attr in Individuo.TABLE.columns:
            is_real = attr.lower() in real_columns 
            operator = "==" if not is_real else choice(["<", ">"])
            real_value = random() * 10000
            bool_value = choice([0, 1, 2, 3])
            value = real_value if is_real else bool_value
            gene = Gene(attr, operator, value, "real" if is_real else "booleano")
            dna.append(gene)
        self.dna = dna

    def __str__(self):
        for i in self.dna:
            print(str(i))