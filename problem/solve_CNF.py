from algorithm.CNF import SatSolver
import random


class CNF:
    def __init__(self, N: int = 8, list: list = []) -> None:
        self.size = N
        self.initCNF = list

    # Convert from coordinate to value of position
    def get_pos(self, x: int, y: int) -> int:
        return x * self.size + y + 1

    # Convert from value of position to coordinate
    def get_coor(self, pos: int) -> tuple[int, int]:
        pos -= 1
        return pos // self.size, pos % self.size  # [column, row]

    def queenCNF(self, row: int, col: int):
        cnf = [[self.get_pos(row, col)]]

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
# 1 2  3  4
# 5 6  7  8
# 9 10 11 12
# 13 14 15 16

    def cnfLevel1(self, x: int, y: int):
        # Check if coordinate is beyond the scope of board or not
        # if (x < 0) or (y < 0) or (x >= self.size) or (y >= self.size):
        #     return []

        list_of_cnf = []
        count = 0
        list_of_cnf.append(self.get_pos(x, y))
        for col in range(self.size):
            if col == x:
                continue
            list_of_cnf.append([-self.get_pos(col, y)])

        for row in range(self.size):
            if row == y:
                continue
            list_of_cnf.append([-self.get_pos(x, row)])

        for i in range(self.size):
            m_diagonal = i - x + y
            if m_diagonal < 0 or m_diagonal >= self.size or (i == x and m_diagonal == y):
                continue
            list_of_cnf.append([-self.get_pos(i, m_diagonal)])

        for i in range(self.size):
            s_diagonal = x + y - i
            if s_diagonal < 0 or s_diagonal >= self.size or (i == x and s_diagonal == y):
                continue
            list_of_cnf.append([-self.get_pos(i, s_diagonal)])
        return list_of_cnf

    # def solveLevel1(self):

    #     #row = [random.randint(0, self.size - 1)*self.size + c + 1 for c in range(self.size)]
    #     oke = SatSolver(self.cnfLevel1(0,0))
    #     return oke

    def solveLevel1(self, x: int, y: int):
        cnf = self.initCNF

        case = []
        row = [random.randint(0, self.size-1)*self.size +
               c + 1 for c in range(self.size)]
        while len(case) < pow(self.size, self.size):
            print('\n')
            while row in case:
                row = [random.randint(0, self.size-1) *
                       self.size + c + 1 for c in range(self.size)]
            case.append(row) 
            print(case)

            hold = cnf.copy()
            for i in range(len(row)):
                hold = add(self.cnfLevel1((row[i]-1) // self.size, i), hold)

            print(hold)
            solution = SatSolver(hold)
            if solution != [] or len(solution) == self.size:
                print(solution)
                return solution, case, cnf

        return [], None, cnf

    def attackCNF(self):
        cnf = []

        for r in range(self.size):
            for c in range(self.size):
                v = self.get_pos(r, c)

                i = 1
                while c + i < self.size:
                    cnf.append([-v, -self.get_pos(r, c+i)])
                    i += 1

                i = 1
                while r + i < self.size:
                    cnf.append([-v, -self.get_pos(r+i, c)])
                    i += 1

                i = 1
                while r + i < self.size and c + i < self.size:
                    cnf.append([-v, -self.get_pos(r+i, c+i)])
                    i += 1

                i = 1
                while r + i < self.size and c - i >= 0:
                    cnf.append([-v, -self.get_pos(r+i, c-i)])
                    i += 1

        return cnf


def add(src: list, dest: list) -> list:
    for i in src:
        dest.append(i)
    return dest
