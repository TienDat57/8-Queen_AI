from pysat.solvers import Solver
import random


class CNF:
    def __init__(self, N: int = 8, list: list = []) -> None:
        self.size = N
        self.initCNF = list

    def getPos(self, x: int, y: int) -> int:
        return x * self.size + y + 1

    def getCoor(self, pos: int) -> tuple[int, int]:
        pos -= 1
        return pos // self.size, pos % self.size  # [column, row]

    def cnfLevel1(self, x: int, y: int):
        if (x < 0) or (y < 0) or (x >= self.size) or (y >= self.size):
            return []
        listOfCnf = [[self.getPos(x, y)]]
        for col in range(self.size):
            if col == x:
                continue
            listOfCnf.append([-self.getPos(col, y)])
        for row in range(self.size):
            if row == y:
                continue
            listOfCnf.append([-self.getPos(x, row)])
        for i in range(self.size):
            m_diagonal = i - x + y
            if m_diagonal < 0 or m_diagonal >= self.size or (i == x and m_diagonal == y):
                continue
            listOfCnf.append([-self.getPos(i, m_diagonal)])
        for i in range(self.size):
            s_diagonal = x + y - i
            if s_diagonal < 0 or s_diagonal >= self.size or (i == x and s_diagonal == y):
                continue
            listOfCnf.append([-self.getPos(i, s_diagonal)])
        return listOfCnf

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