from utils import *

##########################################################
#########   Min-Conflicts   ##############################
##########################################################

def min_conflicts(problem, printResult, max_steps=1000):
    current = {}
    for var in problem.vars:
        val = min_conflicts_value(problem, var, current)
        #current[var] = val
        problem.assign(var, val, current)
    for i in range(max_steps):
        conflicted = problem.conflicted_vars(current)
        if not conflicted:
            if printResult:
                problem.display(current)
                print "Steps to solution", i
                return current
            else:
                return i
        var = random.choice(conflicted)
        val = min_conflicts_value(problem, var, current)
        problem.assign(var, val, current)
    print "No solution"
    return None

def min_conflicts_value(problem, var, current):
    return argmin_random_tie(problem.domains[var],
                             lambda val: problem.nconflicts(var, val, current))
