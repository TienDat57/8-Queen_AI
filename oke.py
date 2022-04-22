# import graphic as gr

# pr = Program()
# # print(pr.readFile("./Input/input1.txt"))
# gr.run()

from Astar.A_star import *
from program import Program

problemAstar = astar(4, [1])

print(problemAstar.solve_astar())