def printMessage(message):
    print("\u001b[36m \n ------------ " + message + " ---------------\n \u001b[0m")

import statistics
def logPop(pop, problem):
    printMessage("População")
    print(str(pop))

    printMessage("Média Fitness")
    evals = pop.eval(problem, [])
    print(statistics.mean(evals))

    printMessage("Pais da seleção")
    parents = pop.selection()
    for p in parents:
        print(p.dna)

