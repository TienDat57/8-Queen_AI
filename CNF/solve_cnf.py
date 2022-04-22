import random
from pysat.solvers import Solver


class CNF:
    def __init__(self, N: int = 8, list: list = []) -> None:
        self.size = N
        self.initCNF = list

    def get_pos(self, x: int, y: int) -> int:
        return x * self.size + y + 1

    def get_coor(self, pos: int) -> tuple[int, int]:
        return (pos - 1) // self.size, (pos - 1) % self.size  # [column, row]

    def cnf_level1(self, x: int, y: int)-> list[list[int]]:
        if (x < 0) or (y < 0) or (x >= self.size) or (y >= self.size):
            return []
        listOfCnf = [[self.get_pos(x, y)]]
        for col in range(self.size):
            if col == x:
                continue
            listOfCnf.append([-self.get_pos(col, y)])
        for row in range(self.size):
            if row == y:
                continue
            listOfCnf.append([-self.get_pos(x, row)])
        for i in range(self.size):
            m_diagonal = i - x + y
            if m_diagonal < 0 or m_diagonal >= self.size or (i == x and m_diagonal == y):
                continue
            listOfCnf.append([-self.get_pos(i, m_diagonal)])
            
            s_diagonal = x + y - i
            if s_diagonal < 0 or s_diagonal >= self.size or (i == x and s_diagonal == y):
                continue
            listOfCnf.append([-self.get_pos(i, s_diagonal)])
        return listOfCnf


    def cnf_level2(self)-> list[list[int]]:
        listOfCnf = []
        for i in range(self.size):
            listOfCnf.append([self.get_pos(i, j) for j in range(0, self.size)])

        for i in range(self.size):
            for j in range(self.size):
                for i1 in range(i + 1, self.size):
                    for j1 in range(j + 1, self.size):
                        if (i - j) == (i1 - j1):
                            listOfCnf.append([-self.get_pos(i, j), -self.get_pos(i1, j1)])
        for i in range(self.size):
            for j in range(self.size):
                for k in range(j + 1, self.size):
                    listOfCnf.append([-self.get_pos(i, j), -self.get_pos(i, k)])
        for i in range(self.size):
            for j in range(self.size):
                for k in range(j + 1, self.size):
                    listOfCnf.append([-self.get_pos(j, i), -self.get_pos(k, i)])

        for i in range(self.size):
            for j in range(self.size):
                for i1 in range(self.size):
                    for j1 in range(self.size):
                        if (i != i1) and (j != j1) and (i + j) == (i1 + j1):
                            listOfCnf.append([-self.get_pos(i, j), -self.get_pos(i1, j1)])
        return listOfCnf
    
    def solve_level1(self):
        cnf = self.initCNF
        case = []
        row = [column + 1 for column in range(self.size)]
        while len(case) < pow(self.size, self.size):
            while row in case:
                row = [random.randint(0, self.size-1) *
                    self.size + c + 1 for c in range(self.size)]
            case.append(row)
        
            hold = cnf.copy()
            for i in range(len(row)):
                hold = add(self.cnf_level1((row[i]-1) // self.size, i), hold)
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

    def solve_level2(self):
        cnf = self.initCNF
        cnf = self.cnf_level2()
        
        #for i in range(self.size):
        #    cnf.append([self.index(i,c) for c in range(self.size)])
        
        #   cnf.append([self.index(r,i) for r in range(self.size)])
        
        s = Solver()
        for clause in cnf:
            s.add_clause(clause)

        cnf.solve()
        solution = []
        if cnf.get_status() == True:
            m = s.get_model()
            solution = [q for q in m if q > 0]

        if solution != [] or len(solution) == self.size:
            return solution, [solution], cnf

        return [], None, cnf
    
def add(src: list, dest: list) -> list:
    for i in src:
        dest.append(i)
    return dest