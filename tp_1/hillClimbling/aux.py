from random import random


def printVector(a: list):
    return str(', '.join(str(e) for e in a))


def noise(min_value, max_value):
    random_dist = random()
    random_value = (max_value - min_value) * random_dist + min_value
    return random_dist, random_value
