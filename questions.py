from typing import List
from variable import Variable
import math
from question import Question

questions = []

## Questão 1
def function_1(args:List[Variable]):
    x = args[0].value
    y = args[1].value
    return math.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1

#a

x = Variable('x', -1.5, 4)
y = Variable('y', -3, 4)
questions.append(Question(function_1, [x,y]))

#b
x = Variable('x', -1, 0)
y = Variable('y', -2, -1)
questions.append(Question(function_1, [x,y]))


##Questão 2
def function2(args:List[Variable]):
    x = args[0].value
    y = args[1].value
    return - (y + 47) * math.sin(math.sqrt(abs((x / 2) + (y + 47)))) - x * math.sin(math.sqrt(abs(x - (y + 47))))

#a
x = Variable('x', -512, 512)
y = Variable('y', -512, 512)
questions.append(Question(function2, [x,y]))

#b
x = Variable('x', 511, 512)
y = Variable('y', 404, 405)
questions.append(Question(function2, [x,y]))

