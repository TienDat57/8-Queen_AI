from algorithm.CNF import SatSolver
import random

class CNF:
    def __init__(self, N :int = 8, list: list = []) -> None:
        self.size = N
        self.initCNF = list

    # Convert from coordinate to value of position
    def get_pos(self, x: int, y: int ) -> int:
        return x * self.size + y + 1

    # Convert from value of position to coordinate
    def get_coor(self, pos: int ) -> tuple[int, int]:
      pos -= 1
      return pos // self.size, pos % self.size #[column, row]

    def queenCNF(self, row:int, col:int):
        cnf = [[self.get_pos(row,col)]]

        for r in range(self.size):
            if r != row:
                cnf.append([-self.get_pos(r, col)])

        for c in range(self.size):
            if c != col:
                cnf.append([-self.get_pos(row, c)])

        i = 1
        while row-i >= 0 and col-i >= 0:
            cnf.append([-self.get_pos(row-i, col-i)])
            i += 1

        i = 1
        while row+i < self.size and col+i < self.size:
            cnf.append([-self.get_pos(row+i, col+i)])
            i += 1

        i = 1
        while row-i >= 0 and col+i < self.size:
            cnf.append([-self.get_pos(row-i, col+i)])
            i += 1

        i = 1
        while row+i < self.size and col-i >= 0:
            cnf.append([-self.get_pos(row+i, col-i)])
            i += 1

        return cnf
    def cnfLevel1(self, x: int, y: int) -> list[list[int]]:
        if (x < 0) or (y < 0) or (x >= self.size) or (y >= self.size): # Check if coordinate is beyond the scope of board or not
            return []

        list_of_cnf = []

        # Consider the case of column
        for col in range(self.size):
            if col == x:
                continue
            list_of_cnf.append([-self.get_pos(x, y), -self.get_pos(col, y)])

        for row in range(self.size):
            if row == y:
                continue
            list_of_cnf.append([-self.get_pos(x, y), -self.get_pos(x, row)])

        for i in range(self.size):
            m_diagonal = i - x + y
            if m_diagonal < 0 or m_diagonal >= self.size or (i == x and m_diagonal == y):
                continue
            list_of_cnf.append([-self.get_pos(x, y), -self.get_pos(i, m_diagonal)])

        for i in range(self.size):
            s_diagonal = x + y - i
            if s_diagonal < 0 or s_diagonal >= self.size or (i == x and s_diagonal == y):
                continue    
            list_of_cnf.append([-self.get_pos(x, y), -self.get_pos(i, s_diagonal)])
        return list_of_cnf

        
    def solveLevel1(self):
        
        #row = [random.randint(0, self.size - 1)*self.size + c + 1 for c in range(self.size)]
        
        return SatSolver(self.cnfLevel1(0, 0))
        

def add(src: list, dest: list) -> list:
    for i in src:
        dest.append(i)
    return dest
