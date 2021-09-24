def printMessage(message):
    print("\u001b[36m \n ------------ " + message + " ---------------\n \u001b[0m")


import statistics


def printPop(pop, problem):
    printMessage("População")
    print(str(pop))

    printMessage("Média Fitness")
    evals = pop.eval(problem)
    print(statistics.mean(evals))


def printVector(list):
    print(str(', '.join(str(e) for e in list)))
