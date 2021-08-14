class Variable:
    def __init__(self, label, li, ls, ri=1, value:float=0):
        self.label = label
        self.li = li
        self.ls = ls
        self.ri = ri
        self.value = value

    def __str__(self):
        return "{:10.3f}".format(self.value)