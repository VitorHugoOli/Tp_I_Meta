from typing import List


class Variable:
    def __init__(self, label, li, ls, ri=1, value: float = 0):
        self.label = label
        self.li = li
        self.ls = ls
        self.ri = ri
        self.value = value

    def __str__(self):
        return "{:.3f}".format(self.value)


def copyList(original: List[Variable]):
    return [Variable(obj.label, obj.li, obj.ls, obj.ri, obj.value) for obj in original]
