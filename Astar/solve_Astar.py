from Astar.A_star import astar
from Astar.node import Node
from Astar.state import State
from queue import PriorityQueue

def astar(problem: astar) -> Node:
    frontier = PriorityQueue()
    expanded = []
    path = []
    current = Node(problem.initState)
    if problem.is_goal(current.state):
        return current.state.queens, [current.state.queens]

    frontier.put(problem.evaluation(current), current)

    while not frontier.empty():
        node = frontier.get()[1]
        state = node.state

        if state.queens not in expanded:
            expanded.append(state.queens)

        if problem.isGoal(state):
            return state.queens, expanded

        childs = problem.successor(node)
        for child in childs:
            childState = child.state
            childVal = problem.evaluation(child)
            
            if (state not in path) or (childVal < problem.evaluation(problem, path[state])):
                path[state] = child
                frontier.put((childVal, child))

    return [], []