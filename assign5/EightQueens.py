import minConflicts as mc
import UniversalDict as ud
#######################################################
######   8 Queens Problem   ###########################
#######################################################

class EightQueens():

    def __init__(self):
        self.rows=[0]*8
        self.ups=[0]*(15)
        self.downs=[0]*(15)
        self.nassigns = 0
        self.vars = range(8)
        self.domains = ud.UniversalDict(range(8))

    def nconflicts(self, var, val, assignment): 
        n = len(self.vars)
        c = self.rows[val] + self.downs[var+val] + self.ups[var-val+n-1]
        if assignment.get(var, None) == val:
            c -= 3
        return c

    def assign(self, var, val, assignment):
        oldval = assignment.get(var, None)
        if val != oldval:
            if oldval is not None: # Remove old val if there was one
                self.record_conflict(assignment, var, oldval, -1)
            self.record_conflict(assignment, var, val, +1)
            assignment[var] = val
            self.nassigns += 1


    def unassign(self, var, assignment):
        if var in assignment:
            self.record_conflict(assignment, var, assignment[var], -1)
            del assignment[var]
        
    def record_conflict(self, assignment, var, val, delta):
        n = len(self.vars)
        self.rows[val] += delta
        self.downs[var + val] += delta
        self.ups[var - val + n - 1] += delta

    def conflicted_vars(self, current):
        return [var for var in self.vars
                if self.nconflicts(var, current[var], current) > 0]

    def display(self, assignment):
        n = len(self.vars)
        for val in range(n):
            for var in range(n):
                if assignment.get(var,'') == val: ch = 'Q'
                elif (var+val) % 2 == 0: ch = '.'
                else: ch = '-'
                print ch,
            print '    ',
            for var in range(n):
                if assignment.get(var,'') == val: ch = '*'
                else: ch = ' '
            print       

####################################################
##########   Main   ################################
####################################################
def runThree():
    for i in range(3):
        problem = EightQueens()
        mc.min_conflicts(problem, True)

def runTen():
    vals = []
    for i in range(10):
        problem = EightQueens()
        vals.append(mc.min_conflicts(problem, False))
    total = 0
    average = 0
    for val in vals:
        if val is not None:
            average += val
            total += 1
    average = average / total
    print "Attempted 10 8-Queens problems"
    print "Results:", vals
    print total, "8-Queens problems solved in an average of", average, "steps."

