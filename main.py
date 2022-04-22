from multiprocessing.spawn import import_main_path
import os
from program import Program
from CNF.solve_CNF import CNF, SatSolver

#1 2  3  4
#5 6  7  8
#9 10 11 12
#13 14 15 16

if __name__=='__main__': 
    cnf_solution = CNF(8)
   # print(cnf_solution.cnf_level2())
    res = cnf_solution.cnf_level2()
    final = SatSolver(res)
    print(final)
    