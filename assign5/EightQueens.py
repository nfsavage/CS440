import minConflicts as mc

#######################################################
######   8 Queens Problem   ###########################
#######################################################

class EightQueens():

    def __init__(self):
        """Initialize data structures for n Queens."""
        self.rows=[0]*8
        self.ups=[0]*(15)
        self.downs=[0]*(15)
        self.nassigns = 0
        self.vars = range(8)
        print "Vars"
        print self.vars
        self.domains = UniversalDict(range(8))
        print "domains"
        print self.domains

    def nconflicts(self, var, val, assignment): 
        """The number of conflicts, as recorded with each assignment.
        Count conflicts in row and in up, down diagonals. If there
        is a queen there, it can't conflict with itself, so subtract 3."""
        n = len(self.vars)
        c = self.rows[val] + self.downs[var+val] + self.ups[var-val+n-1]
        if assignment.get(var, None) == val:
            c -= 3
        return c

    def assign(self, var, val, assignment):
        "Assign var, and keep track of conflicts."
        oldval = assignment.get(var, None)
        if val != oldval:
            if oldval is not None: # Remove old val if there was one
                self.record_conflict(assignment, var, oldval, -1)
            self.record_conflict(assignment, var, val, +1)
            assignment[var] = val
            self.nassigns += 1


    def unassign(self, var, assignment):
        "Remove var from assignment (if it is there) and track conflicts."
        if var in assignment:
            self.record_conflict(assignment, var, assignment[var], -1)
            del assignment[var]
        
    def record_conflict(self, assignment, var, val, delta):
        "Record conflicts caused by addition or deletion of a Queen."
        n = len(self.vars)
        self.rows[val] += delta
        self.downs[var + val] += delta
        self.ups[var - val + n - 1] += delta

    def conflicted_vars(self, current):
        "Return a list of variables in current assignment that are in conflict"
        return [var for var in self.vars
                if self.nconflicts(var, current[var], current) > 0]

    def display(self, assignment):
        "Print the queens and the nconflicts values (for debugging)."
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
#                print str(self.nconflicts(var, val, assignment))+ch, 
            print       

####################################################
##########  Dictionary Class #######################
####################################################

class UniversalDict:
    """A universal dict maps any key to the same value. We use it here
    as the domains dict for CSPs in which all vars have the same domain.
    >>> d = UniversalDict(42)
    >>> d['life']
    42
    """
    def __init__(self, value): self.value = value
    def __getitem__(self, key): return self.value
    def __repr__(self): return '{Any: %r}' % self.value



####################################################
##########   Main   ################################
####################################################

if __name__ == "__main__":
    problem = EightQueens()
    #problem.display()
    mc.min_conflicts(problem) 
