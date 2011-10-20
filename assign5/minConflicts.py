from utils import *

##########################################################
#########   Min-Conflicts   ##############################
##########################################################

def min_conflicts(problem, max_steps=1000):
    """Solve a CSP by stochastic hillclimbing on the number of conflicts."""
    # Generate a complete assignment for all vars (probably with conflicts)
    current = {}
    for var in problem.vars:
        val = min_conflicts_value(problem, var, current)
        #current[var] = val
        problem.assign(var, val, current)
    # Now repeatedly choose a random conflicted variable and change it
    for i in range(max_steps):
        conflicted = problem.conflicted_vars(current)
        if not conflicted:
            problem.display(current)
            print "Steps to solution", i
            return current
        var = random.choice(conflicted)
        val = min_conflicts_value(problem, var, current)
        #current[var] = val
        problem.assign(var, val, current)
    #problem.display(current)
    print "No solution"
    return None

def min_conflicts_value(problem, var, current):
    """Return the value that will give var the least number of conflicts.
    If there is a tie, choose at random."""
    return argmin_random_tie(problem.domains[var],
                             lambda val: problem.nconflicts(var, val, current))
"""
class MinCHelper():

    def _init_(self, vars, domains ):
        vars = vars or domains.keys()
        update(self, vars=vars, domains=domains, nassigns=0)

    def assign(self, var, val, assignment):
        assignment[var] = val
        self.nassigns += 1

    def nconflicts(self, var, val, assignment):
        def conflict(var2)
            val2 = assignment.get(var2, None)
            return val2 != None and not self.contraints(var, val, var2, val2)
        return count_if(conflict, self.neighbors[var])

    def conflicted_vars(selfm current):
        return [var for var in self.vars if self.nconflicts(var, current[var], current) > 0]"""
