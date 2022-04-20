from Astar.solve_Astar import Astar
from Astar.node import Node
from Astar.state import State
from program import Program
from CNF.cnf import CNF
import os
import random

class Astar:
    def __init__(self, size:int=0, initQueens:list=[]) -> None:
        self.size = size
        self.initState = State(initQueens)

    def frontier(self, node:Node) -> list:
        frontier_list = []

        if len(node.state.queens) == self.size:
            return frontier_list

        chess_board = node.state.initBoard(self.size)

        for row in range(self.size):
            for col in range(self.size):
                if (row*self.size + col + 1) not in node.state.queens:
                    queens = node.state.queens.copy()
                    queens.append(CNF.getPos(row,col))
                    state = State(queens)
                    path_cost = self.cost_function(node.state, state) + node.path_cost
                    childNode = Node(state, path_cost, node)
                    frontier_list.append(childNode)

        return frontier_list
    
    def isGoal(self, state:State):
        if len(state.queens) != self.size:
            return False
        for i in range(len(state.queens)):
            j = i + 1
            for j in range(len(state.queens)):
                if self.isAttack(state.queens[i], state.queens[j]):
                    return False
        return True

    def isAttack(self, pos_queen1:int, pos_queen2:int) -> bool:
        row_queen1 = (pos_queen1 - 1) // self.size
        col_queen1 = (pos_queen1 - 1) %  self.size
        row_queen2 = (pos_queen2 - 1) // self.size
        col_queen2 = (pos_queen2 - 1) %  self.size

        if row_queen1 == row_queen2: return True
        if col_queen1 == col_queen2: return True
        if (row_queen1 + col_queen1) == (row_queen2 + col_queen2): return True
        if (row_queen1 - col_queen1) == (row_queen2 - col_queen2): return True
        return False

    def evaluation(self, node:Node) -> int:
        return node.path_cost + self.heuristic(node.state)

    def cost_function(self, pre_state:State, state:State) -> int:
        # # num_queen_attack = 0
        # # for i in range(0, len(state.queens)):
        # #     for j in range(i+1, len(state.queens)):
        # #         if self.isAttack(state.queens[i], state.queens[j]):
        # #             num_queen_attack += 1
        # # return len(state.queens) + num_queen_attack
        # return self.size - len(state.queens)
        return 1

    def heuristic(self, state:State) -> int:
        num_queen_attack = 0
        for i in range(0, len(state.queens)):
            for j in range(i+1, len(state.queens)):
                if self.isAttack(state.queens[i], state.queens[j]):
                    num_queen_attack += 1
        return num_queen_attack
