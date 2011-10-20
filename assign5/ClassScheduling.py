import minConflicts as mc
import UniversalDict as ud

####################################################
######   Class Room Scheduling   ###################
####################################################

class ClassScheduling():
    
    def __init__(self):
        self.nassigns = 0
        self.vars =    ["CS160",
                        "CS161",
                        "CS200",
                        "CS270",
                        "CS253",
                        "CS320",
                        "CS314",
                        "CS410",
                        "CS430",
                        "CS440"]
        self.domains = ud.UniversalDict([("CSB130", 9),
                                         ("CSB130", 10),
                                         ("CSB130", 11),
                                         ("CSB130", 12),
                                         ("CSB130", 1),
                                         ("CSB425", 9),
                                         ("CSB425", 10),
                                         ("CSB425", 11),
                                         ("CSB425", 12),
                                         ("CSB425", 1)]) 
        self.conflicts={"CS160": None,
                        "CS161": None,
                        "CS200":["CS270", "CS253", "CS320", "CS314"],
                        "CS270":["CS200", "CS253", "CS320", "CS314"],
                        "CS253":["CS200", "CS270", "CS320", "CS314"],
                        "CS320":["CS200", "CS270", "CS253", "CS314"],
                        "CS314":["CS200", "CS270", "CS253", "CS320"],
                        "CS410":["CS430", "CS440"],
                        "CS430":["CS410", "CS440"],
                        "CS440":["CS410", "CS430"]}
    def nconflicts(self, var, val, assignment):
        c = 0
#        if val in assignment.values():
#            c +=1
        if val in assignment.values():
            for key in assignment.keys():
                if key != var:
                    if assignment.get(key, None) == val:
                        c +=1
        if self.conflicts.get(var) is not None:
            for conflict in self.conflicts.get(var):
                assign = assignment.get(conflict)
                if assign is not None:
                    if val[1] == assign[1]:
                        c +=1
        #print c
        return c
        

    def assign(self, var, val, assignment):
        oldval = assignment.get(var, None)
        if val != oldval and oldval == None:
            assignment[var] = val
            self.nassigns += 1

    def unassign(self, var, assignment):
        if var in assinment:
            del assignement[var]

    def conflicted_vars(self, current):
        for var in self.vars:
            if self.nconflicts(var, current.get(var, None), current) > 0:
                return var
        return False 

    def display(self, assignment):
        CSB130 = [None]*5
        CSB425 = [None]*5
        for key in assignment.keys():
            slot = assignment.get(key, None)
            if slot[0] == "CSB130":
                if slot[1] == 1:
                    CSB130[4] = key
                else:
                    CSB130[slot[1]%9] = key
            else:
                if slot[1] == 1:
                    CSB425[4] = key
                else:
                    CSB425[slot[1]%9] = key
        print "    CSB 130      CSB 425"
        print "------------------------------------"
        for i in range(5):
            if i < 4:
                if i == 0:
                    print" 9", "  ", CSB130[i], "     ", CSB425[i]
                else:
                    print 9+i,"  ", CSB130[i], "     ", CSB425[i]
            else:
                print " 1", "  ", CSB130[i], "     ", CSB425[i]
        print

if __name__ == "__main__":
    for i in range(100):
        problem = ClassScheduling()
        mc.min_conflicts(problem)
