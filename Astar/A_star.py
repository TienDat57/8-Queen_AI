from Astar.node import Node
from Astar.state import State
from CNF.cnf import CNF

class astar:
    def __init__(self, size: int = 0, initQueens: list = []) -> None:
        self.size = size
        self.initState = State(initQueens)

    def frontier(self, root: Node) -> list:
        frontier_list = []

        if len(root.state.queens) == self.size:
            return frontier_list

        root.state.init_board(self.size)

        for row in range(self.size):
            for col in range(self.size):
                if (CNF.get_pos(col, row)) not in root.state.queens:
                    queens = root.state.queens.copy()
                    queens.append(CNF.get_pos(col, row))
                    state = State(queens)
                    pathCost = self.cost_function(
                        root.state, state) + root.path_cost
                    childNode = Node(state, pathCost, root)
                    frontier_list.append(childNode)

        return frontier_list

    def is_goal(self, state: State):
        if len(state.queens) != self.size:
            return False
        for i in range(len(state.queens)):
            j = i + 1
            for j in range(len(state.queens)):
                if is_attack(state.queens[i][j], state.queens[j]):
                    return False
        return True

    

    def successor(self, node: Node) -> list:
        childs = []

        if len(node.state.queens) == self.size:
            return childs

        board = node.state.initBoard(self.size)
        childs.append(childNode)

        for row in range(self.size):
            for col in range(self.size):
                if (row*self.size + col + 1) not in node.state.queens:
                    queens = node.state.queens.copy()
                    queens.append(row * self.size + col + 1)
                    state = State(queens)
                    path_cost = self.cost_function(
                        node.state, state) + node.path_cost
                    childNode = Node(state, path_cost, node)
                    childs.append(childNode)

        return childs

    def cost_function(self):
        return 1

    def evaluation(self, node: Node):
        return node.path_cost + self.heuristic(node.state)

    def heuristic(self, state: State):
        num_queen_attack = 0
        for i in range(0, len(state.queens)):
            j = i + 1
            for j in range(len(state.queens)):
                if self.is_attack(state.queens[i], state.queens[j]):
                    num_queen_attack += 1
        return num_queen_attack

def is_attack(queen1: int, queen2: int):
        colQueen1 = (queen1 - 1) // 8
        rowQueen1 = (queen1 - 1) % 8
        colQueen2 = (queen2 - 1) // 8
        rowQueen2 = (queen2 - 1) % 8
        
        if rowQueen1 == rowQueen2:
            return True
        if colQueen1 == colQueen2:
            return True
        return abs(rowQueen1 - rowQueen2) == abs(colQueen1 - colQueen2)