from typing import List

from tp_1.statistics.solver import solver
from hillClimbling.hill_climbing import hill_climbing
from hillClimbling.variable import Variable
import math

questions = []

STATS_LOOPS = 30

'''
Função: f(x)=x² 
Variaveis de entrada: −1.5 ≤ 𝑥 ≤ 4 e −3 ≤ 𝑦 ≤ 4

Função para avaliação do algoritimo
'''


def function_0(x: Variable, y: Variable):
    x = x.value
    y = y.value
    return ((x - 10) ** 3) + ((y - 20) ** 3)


# A) −1.5 ≤ 𝑥 ≤ 4 e −3 ≤ 𝑦 ≤ 4
print("\nFunção: f(x)=x² \nVariaveis de entrada: −1.5 ≤ 𝑥 ≤ 4 e −3 ≤ 𝑦 ≤ 4")
solver(function_0, [Variable('x', -1.5, 4), Variable('y', -3, 4)], STATS_LOOPS, plot_name='x^2', basis_limit=0)

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
solver(function_1, [Variable('x', 13, 100), Variable('y', 0, 100)], STATS_LOOPS, plot_name='function 1_1', basis_limit=0)

# B) −1 ≤ 𝑥 ≤ 0 e −2 ≤ 𝑦 ≤ −1
print("\nFunção: f(x)= sin(𝑥+𝑦) + (𝑥-𝑦)² - 1.5𝑥 + 2.5y + 1 \nVariaveis de entrada: −1 ≤ 𝑥 ≤ 0 e −2 ≤ 𝑦 ≤ −1")
solver(function_1, [Variable('x', -1, 0), Variable('y', -2, -1)], STATS_LOOPS, plot_name='function 1_2', basis_limit=0)

'''
Função: f(x) = -(𝑦 + 47) * math.sin(math.sqrt(abs((𝑥 / 2) + (𝑦 + 47)))) - 𝑥 * math.sin(math.sqrt(abs(𝑥 - (𝑦 + 47)))) 
Variaveis de entrada: −512 ≤ 𝑥,𝑦 ≤ 512 
Variaveis de entrada: 511 ≤ 𝑥 ≤ 512 e 404 ≤ 𝑦 ≤ 405

Questão 2)
'''


def function_2(x: Variable, y: Variable):
    x = x.value
    y = y.value
    return -(y + 47) * math.sin(math.sqrt(abs((x / 2) + (y + 47)))) - x * math.sin(math.sqrt(abs(x - (y + 47))))


# A) −512 ≤ 𝑥,𝑦 ≤ 512
print("\nFunção: f(x) = -(𝑦 + 47) * math.sin(math.sqrt(abs((𝑥 / 2) + (𝑦 + 47)))) - 𝑥 * math.sin(math.sqrt(abs(𝑥 - (𝑦 + 47)))) \nVariaveis de entrada: −512 ≤ 𝑥,𝑦 ≤ 512")
solver(function_2, [Variable('x', -512, 512), Variable('y', -512, 512)], STATS_LOOPS, plot_name='function 2_1', basis_limit=30)

# B) −1 ≤ 𝑥 ≤ 0 e −2 ≤ 𝑦 ≤ −1
print(
    "\nFunção: f(x) = -(𝑦 + 47) * math.sin(math.sqrt(abs((𝑥 / 2) + (𝑦 + 47)))) - 𝑥 * math.sin(math.sqrt(abs(𝑥 - (𝑦 + 47)))) \nVariaveis de entrada: 511 ≤ 𝑥 ≤ 512 e 404 ≤ 𝑦 ≤ 405")
solver(function_2, [Variable('x', 511, 512), Variable('y', 404, 405)], STATS_LOOPS, plot_name='function 2_2', basis_limit=30)
