import math
from restrictions import Restriction
from variable import Variable

units = [
    {'min': 0,  'max': 680, 'a': 0.00028,'b': 8.10,'c': 550, 'e': 300, 'f': 0.0035},
    {'min': 0,  'max': 360, 'a': 0.00056,'b': 8.10,'c': 309, 'e': 200, 'f':0.042 },
    {'min': 0,  'max': 360, 'a': 0.00056,'b': 8.10,'c': 307, 'e': 150, 'f':0.042 },
    {'min': 60, 'max':  180, 'a': 0.00324,'b': 7.74,'c': 240, 'e': 150, 'f':0.063 },
    {'min': 60, 'max':  180 , 'a': 0.00324,'b': 7.74,'c':240 , 'e': 150, 'f':0.063 },
    {'min': 60, 'max':  180 , 'a': 0.00324,'b': 7.74,'c':240 , 'e': 150, 'f':0.063 },
    {'min': 60, 'max':  180 , 'a': 0.00324,'b': 7.74,'c':240 , 'e': 150, 'f':0.063 },
    {'min': 60, 'max':  180 , 'a': 0.00324,'b': 7.74,'c':240 , 'e': 150, 'f':0.063 },
    {'min': 60, 'max':  180 , 'a': 0.00324,'b': 7.74,'c':240 , 'e': 150, 'f':0.063 },
    {'min': 40, 'max':  120 , 'a': 0.00284,'b':8.60 ,'c':126 , 'e': 100, 'f':0.084 },
    {'min': 40, 'max':  120 , 'a': 0.00284,'b':8.60 ,'c':126 , 'e': 100, 'f':0.084 },
    {'min': 55, 'max':  120 , 'a': 0.00284,'b': 8.60,'c':126 , 'e': 100, 'f':0.084 },
    {'min': 55, 'max':  120 , 'a': 0.00284,'b': 8.6,'c':126 , 'e': 100, 'f':0.084 },
]


def P(p_variable:Variable, p, a,b,c,e,f):
    return (a * (p ** 2)) + (b*p) + c + abs(e * math.sin(f *( p_variable.li - p)))

def objective_2(*ps):
    result = 0
    for i in range(13):
        p_variable = Variable(f"P{i}", units[i]['min'], units[i]['max'])
        result += P(p_variable, ps[i] ,units[i]['a'], units[i]['b'], units[i]['c'], units[i]['e'], units[i]['f'])
    return result

def get_variables():
    variables = []
    for i in range(len(units)):
        v = Variable(f'P{i}', units[i]['min'], units[i]['max'])
        variables.append(v)
    return variables

def get_restrictions():
    pass


# 1820 10  
def restriction1(*ps):
    # print(ps)
    epsilon = 0.0000000001
    result = sum(ps)
    # print(f"Olha o result galerainha ==> {result}")
    return result - epsilon - 1800

# 1780 10 
def restriction2(*ps):
    epsilon = 0.0000000001
    result = sum(ps)
    return - result - epsilon + 1800

def get_restrictions(epsilon=0.1):
    restrictions = [Restriction(restriction1, alpha=1), Restriction(restriction2, alpha=1)]
    return restrictions