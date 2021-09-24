import statistics


def printMessage(message):
    print("\u001b[36m \n ------------ " + message + " ---------------\n \u001b[0m")


def printPop(pop, problem):
    printMessage("População")
    print(str(pop))

    printMessage("Média Fitness")
    print(statistics.mean([i.eval_value or 0 for i in pop.population]))


def printVector(list):
    print(str(', '.join(str(e) for e in list)))
