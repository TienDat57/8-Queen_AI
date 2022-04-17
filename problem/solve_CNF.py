from algorithm.CNF import SatSolver
import random

class CNF:

    def __init__(self,  N:int = 8, list: list = []) -> None:
        self.size = N
        self.initCNF = list

    def index(self, row: int, col: int):
        return row*self.size + col + 1

    def getIndexRow(self, idx: int):
        return (idx - 1) // self.size

    def getIndexCol(self, idx: int):
        return (idx - 1) % self.size

    def Level1(self):
        cnf = self.initCNF

        case = []
        row = [random.randint(0, self.size - 1)*self.size + c + 1 for c in range(self.size)]
        while len(case) < self.size**2:
            while row in case:
                row = [random.randint(0, self.size - 1)*self.size + c + 1 for c in range(self.size)]
            case.append(row)

            hold = cnf.copy()
            for i in range(len(row)):
                hold = add(self.constraintCNF((row[i]-1) // self.size, i), hold)

            solution = SatSolver(hold)
            if solution != [] or len(solution) == self.size:
                return solution, case, cnf

        return [], None, cnf

    def constraintCNF(self, row:int, col:int):
        cnf = [[self.index(row,col)]]

        for r in range(self.size):
            if r != row:
                cnf.append([-self.index(r, col)])

        for c in range(self.size):
            if c != col:
                cnf.append([-self.index(row, c)])

        i = 1
        while row-i >= 0 and col-i >= 0:
            cnf.append([-self.index(row-i, col-i)])
            i += 1

        i = 1
        while row+i < self.size and col+i < self.size:
            cnf.append([-self.index(row+i, col+i)])
            i += 1

        i = 1
        while row-i >= 0 and col+i < self.size:
            cnf.append([-self.index(row-i, col+i)])
            i += 1

        i = 1
        while row+i < self.size and col-i >= 0:
            cnf.append([-self.index(row+i, col-i)])
            i += 1

        return cnf
    
def add(src: list, dest: list) -> list:
    return [dest.append(i) for i in src]
