import random
from pysat.solvers import Solver

def solveLevel1(self):
        cnf = self.initCNF
        case = []
        row = [random.randint(0, self.size-1)*self.size +
               column + 1 for column in range(self.size)]
        while len(case) < pow(self.size, self.size):
            while row in case:
                row = [random.randint(0, self.size-1) *
                       self.size + c + 1 for c in range(self.size)]
            case.append(row)
            print(case)
            hold = cnf.copy()
            for i in range(len(row)):
                hold = add(self.cnfLevel1((row[i]-1) // self.size, i), hold)
            s = Solver()
            for clause in hold:
                s.add_clause(clause)

            s.solve()
            solution = []
            if s.get_status() == True:
                m = s.get_model()
                solution = [q for q in m if q > 0]

            if solution != [] or len(solution) == self.size:
                return [q for q in m if q > 0], case, cnf
        return [], None, cnf

def add(src: list, dest: list) -> list:
    for i in src:
        dest.append(i)
    return dest