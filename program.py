import os
from problem.solve_CNF import CNF

class Program:
    def __init__(self, n:int) -> None:
        self.numQueen = n

    def solveCNF(self):
        self.cnf_problem = CNF(self.numQueen, self.clause)
        self.cnf_solution1 = self.cnf_problem.solveLevel1()
        # self.cnf_solution2 = self.cnf_problem.solveLevel2()

    def InputCNF(self, filename):
        filename += ".txt"
        if os.path.isfile(os.path.join('./Input/cnf', filename)):
            self.finput = filename.replace(".txt", "")
            filepath = os.path.join('./Input/cnf', filename)
            N, clause = self.readFileCNF(filepath)
            if N != None and clause != None:
                self.size = N
                self.clause = clause
                return True
        print('Invalid filename')
        return False

    def readFileCNF(self, filepath):
        if not os.path.exists(filepath):
            return None, None
        
        file = open(filepath, "r")

        N = (int)(file.readline())
        cnf = []
        for _ in range(N):
            line = file.readline()
            tmp = line.split(' ')
            if len(tmp) == 2:
                cor = [int(x) for x in tmp]
                cnf.append([cor[0]*self.numQueen + cor[1] + 1])
            elif len(tmp) == 3:
                cor = [int(tmp[i]) for i in range(1, len(tmp))]
                cnf.append([-(cor[0]*self.numQueen + cor[1] + 1)])

        file.close()
        return N, cnf
    
    def positionToIndex(self, position:list):
        return [(pos[0] * self.numQueen + pos[1] + 1) for pos in position]
    
    def indexToPosition(self, idx:list):
        position = []
        for i in idx:
            row = (i - 1) // self.numQueen
            col = (i - 1) % self.numQueen
            position.append([row, col])
        return position


