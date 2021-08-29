from typing import List

from Statistics.solver import solver
from hillClimbling.hill_climbing import hill_climbing
from hillClimbling.variable import Variable
import math

questions = []

STATS_LOOPS = 5

'''
Função: f(x)=x² 
Variaveis de entrada: −1.5 ≤ 𝑥 ≤ 4 e −3 ≤ 𝑦 ≤ 4


Função para avaliação do algoritimo
'''


def function_0(x: Variable, y: Variable):
    x = x.value
    y = y.value
    return x ** 2


# A) −1.5 ≤ 𝑥 ≤ 4 e −3 ≤ 𝑦 ≤ 4
print("\nFunção: f(x)=x² \nVariaveis de entrada: −1.5 ≤ 𝑥 ≤ 4 e −3 ≤ 𝑦 ≤ 4")
solver(function_0, [Variable('x', -1.5, 4), Variable('y', -3, 4)], STATS_LOOPS)

# B) −1 ≤ 𝑥 ≤ 0 e −2 ≤ 𝑦 ≤ −1
print("\nFunção: f(x)=x² \nVariaveis de entrada: −1 ≤ 𝑥 ≤ 0 e −2 ≤ 𝑦 ≤ −1")
solver(function_0, [Variable('x', -1, 0), Variable('y', -2, -1)], STATS_LOOPS)

'''
Função: f(x)= sin(𝑥+𝑦) + (𝑥-𝑦)² - 1.5𝑥 + 2.5y + 1 
Variaveis de entrada: −1.5 ≤ 𝑥 ≤ 4 e −3 ≤ 𝑦 ≤ 4
Variaveis de entrada: −1 ≤ 𝑥 ≤ 0 e −2 ≤ 𝑦 ≤ −1

Questão 1)
'''


def function_1(x: Variable, y: Variable):
    x = x.value
    y = y.value
    return math.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1


# A) −1.5 ≤ 𝑥 ≤ 4 e −3 ≤ 𝑦 ≤ 4
print("\nFunção: f(x)= sin(𝑥+𝑦) + (𝑥-𝑦)² - 1.5𝑥 + 2.5y + 1 \nVariaveis de entrada: −1.5 ≤ 𝑥 ≤ 4 e −3 ≤ 𝑦 ≤ 4")
solver(function_1, [Variable('x', -1.5, 4), Variable('y', -3, 4)], STATS_LOOPS)

# B) −1 ≤ 𝑥 ≤ 0 e −2 ≤ 𝑦 ≤ −1
print("\nFunção: f(x)= sin(𝑥+𝑦) + (𝑥-𝑦)² - 1.5𝑥 + 2.5y + 1 \nVariaveis de entrada: −1 ≤ 𝑥 ≤ 0 e −2 ≤ 𝑦 ≤ −1")
solver(function_1, [Variable('x', -1, 0), Variable('y', -2, -1)], STATS_LOOPS)

'''
Função: f(x)= sin(𝑥+𝑦) + (𝑥-𝑦)² - 1.5𝑥 + 2.5𝑦 + 1 
Variaveis de entrada: −512 ≤ 𝑥,𝑦 ≤ 512 
Variaveis de entrada: 511 ≤ 𝑥 ≤ 512 e 404 ≤ 𝑦 ≤ 405

Questão 2)
'''


def function_2(x: Variable, y: Variable):
    x = x.value
    y = y.value
    return math.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1


# A) −512 ≤ 𝑥,𝑦 ≤ 512
print("\nFunção: f(x)= sin(𝑥+𝑦) + (𝑥-𝑦)² - 1.5𝑥 + 2.5𝑦 + 1 \nVariaveis de entrada: −512 ≤ 𝑥,𝑦 ≤ 512 ")
solver(function_2, [Variable('x', -512, 512), Variable('y', -512, 512)], STATS_LOOPS)

# B) −1 ≤ 𝑥 ≤ 0 e −2 ≤ 𝑦 ≤ −1
print("\nFunção: f(x)= sin(𝑥+𝑦) + (𝑥-𝑦)² - 1.5𝑥 + 2.5𝑦 + 1 \nVariaveis de entrada: 511 ≤ 𝑥 ≤ 512 e 404 ≤ 𝑦 ≤ 405")
solver(function_2, [Variable('x', 511, 512), Variable('y', 404, 405)], STATS_LOOPS)
