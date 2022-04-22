import random
from pysat.solvers import Solver

def SatSolver(clauses):
    s = Solver()

    for clause in clauses:
        s.add_clause(clause)

    s.solve()

    if s.get_status():
        m = s.get_model()
        return [q for q in m if q > 0]

    return []

class CNF:
    def __init__(self, N: int = 8, list: list = []) -> None:
        self.size = N
        self.initCNF = list

    def get_pos(self, x: int, y: int) -> int:
        return x * self.size + y + 1

    def get_coor(self, pos: int) -> tuple[int, int]:
        return (pos - 1) // self.size, (pos - 1) % self.size  # [column, row]

    
    def cnf_level2(self) -> list[list[int]]:
        cnf = []
        for i in range(1,9):
           cnf.append([self.get_pos(i,j) for j in range(1, 9)])
           cnf.append([self.get_pos(j,i) for j in range(1,9)])
           
        for i in range(1,9):
            for j in range(1,9):
                for k in range(j + 1,9):
                    cnf.append([-self.get_pos(i,j),-self.get_pos(i,k)])
        for i in range(1,9):
            for j in range(1,9):
                for k in range(j+1,9):
                    cnf.append([-self.get_pos(j,i),-self.get_pos(k,i)])
        for i in range(1,9):
            for j in range(1,9):
                for i1 in range(i+1,9):
                    for j1 in range(j+1,9):
                        if (i-j)==(i1-j1):
                            cnf.append([-self.get_pos(i,j),-self.get_pos(i1,j1)])
        for i in range(1, 9):
            for j in range(1, 9):
                for i1 in range(1, 9):
                    for j1 in range(1, 9):
                        if (i!=i1) and (j!=j1) and (i+j)==(i1+j1):
                            cnf.append([-self.get_pos(i,j),-self.get_pos(i1,j1)])
        return cnf
    
    def cnf_level1(self) -> list[list[int]]:   
        cnf = []
        for i in range(self.size):
           cnf.append([self.get_pos(i,j) for j in range(1,9)])
           cnf.append([self.get_pos(j,i) for j in range(1,9)])
           
        for i in range(self.size):
            for j in range(self.size):
                for k in range(j + 1, self.size):
                    cnf.append([-self.get_pos(i,j),-self.get_pos(i,k)])

        for i in range(self.size):
            for j in range(self.size):
                for i1 in range(i+1,self.size):
                    for j1 in range(j+1,self.size):
                        if (i-j)==(i1-j1):
                            cnf.append([-self.get_pos(i,j),-self.get_pos(i1,j1)])
                            
        for i in range(self.size):
            for j in range(self.size):
                for i1 in range(self.size):
                    for j1 in range(self.size):
                        if (i!=i1) and (j!=j1) and (i+j)==(i1+j1):
                            cnf.append([-self.get_pos(i,j),-self.get_pos(i1,j1)])
        return cnf

def add(src: list, dest: list) -> list:
    for i in src:
        dest.append(i)
    return dest
