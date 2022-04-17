import os
from program import Program
from problem.solve_CNF import CNF
if __name__=='__main__': 
    program = Program(4)

    os.system("cls")
    INPUT_DIR = './Input/cnf'
    files = [name.replace('.txt', '') for name in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, name))]

    print('Available input files: ', end='  ')
    # sFile = ''
    # for file in files:
    #   sFile += file + '    '
    # print(sFile)

    inputValid = False
    while not inputValid:
        file = input("Enter filename: ")
        inputValid = program.InputCNF(filename=file)

    program.solveCNF()
    print("CNF: ", program.cnf_solution1[2])