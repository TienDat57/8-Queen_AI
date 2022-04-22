import os
from CNF.solve_CNF import CNF

class Program:
    def __init__(self, n: int = 0) -> None:
        self.numQueen = n

    def solveCNF(self):
        self.cnf_problem = CNF(self.numQueen, self.clause)
        self.cnf_solution1 = CNF.solve_level1(self.cnf_problem)
        # self.cnf_solution2 = self.cnf_problem.solveLevel2()

    def InputCNF(self, filename):
        filename += ".txt"
        if os.path.isfile(os.path.join('./Input', filename)):
            self.finput = filename.replace(".txt", "")
            filepath = os.path.join('./Input', filename)
            N, clause = self.readFile(filepath)

            if N != None and clause != None:
                self.size = N
                self.clause = clause
                return True
        print('Invalid filename')
        return False

    def readFile(self, fileName):
        if not os.path.exists(fileName):
            return None
        file = open(fileName, "r")
        arrayRes = [()]
        N = (int)(file.readline())   # number of queens
        self.numQueen = N
        line = file.readline()
        invalidCharacters = "(,)"
        for character in invalidCharacters:
            line = line.replace(character, "")
        tempArr = [int(x) for x in line.split(' ')]   # [0]=1 [1]=2 [2]=3 [3]=4
        arrayRes = [x for x in zip(*[iter(tempArr)]*2)]
        file.close()
        return arrayRes

    def positionToIndex(self, position: list):
        return [(pos[0] * self.numQueen + pos[1] + 1) for pos in position]

    def indexToPosition(self, idx: list):
        position = []
        for i in idx:
            row = (i - 1) // self.numQueen
            col = (i - 1) % self.numQueen
            position.append([row, col])
        return position
    
    
