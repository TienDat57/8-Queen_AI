from multiprocessing.spawn import import_main_path
import os
from program import Program
from CNF.solve_CNF import CNF

if __name__=='__main__': 
    problem = CNF(4, [])
    solution = problem.solve_level1()
    print(solution)
    
    # print(problem.cnfLevel1(0, 0))
    #print(solution)
    #os.system("cls")
    #INPUT_DIR = './Input/input1'
    #files = [name.replace('.txt', '') for name in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, name))]

    # print('Available input files: ', end='  ')
    # sFile = ''
    # for file in files:
    #   sFile += file + '    '
    # print(sFile)

    # inputValid = False
   
    #file = input("Enter filename: ")
    #inputValid = program.InputCNF(filename=file)
    
    #program.cnf_solution1
    #print("CNF: ", program.cnf_solution1[2])