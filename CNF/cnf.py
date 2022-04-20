from pysat.solvers import Solver

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

    def cnf_level2(self)-> list[list[int]]:
        listOfCnf = []
        for i in range(1, 9):
            listOfCnf.append([self.getPos(i, j) for j in range(1, 9)])

        for i in range(1, 9):
            for j in range(1, 9):
                for i1 in range(i + 1, 9):
                    for j1 in range(j + 1, 9):
                        if (i - j) == (i1 - j1):
                            listOfCnf.append([-self.getPos(i, j), -self.getPos(i1, j1)])
        for i in range(1, 9):
            for j in range(1, 9):
                for k in range(j + 1, 9):
                    listOfCnf.append([-self.getPos(i, j), -self.getPos(i, k)])
        for i in range(1, 9):
            for j in range(1, 9):
                for k in range(j + 1, 9):
                    listOfCnf.append([-self.getPos(j, i), -self.getPos(k, i)])

        for i in range(1, 9):
            for j in range(1, 9):
                for i1 in range(1, 9):
                    for j1 in range(1, 9):
                        if (i != i1) and (j != j1) and (i + j) == (i1 + j1):
                            listOfCnf.append([-self.getPos(i, j), -self.getPos(i1, j1)])
        return listOfCnf

    
