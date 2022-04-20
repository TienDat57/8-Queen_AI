import random
from CNF.cnf import cnf

class State:
    '''

    '''
    def __init__(self, queens: list = []) -> None:
        self.queens = queens
        
    def initBoard(self, size: int):
        chess_board = [[]]
        for i in range(size):
            for j in range(size):
                chess_board[i][j] = True
        
        for queen in self.queens:
            coor = cnf.getCoor(queen)
            col = coor[0] 
            row = coor[1]

            for i in range(size):
                chess_board[i][col] = False # column
                chess_board[row][i] = False # row

                # main diagonal
                m_diagonal = i - col + row
                if m_diagonal < 0 or m_diagonal >= self.size or (i == col and m_diagonal == row):
                    continue
                chess_board[i][m_diagonal] = False
                
                # sub diagonal
                s_diagonal = col + row - i
                if s_diagonal < 0 or s_diagonal >= self.size or (i == col and s_diagonal == row):
                    continue
                chess_board[i][s_diagonal] = False

        return chess_board
    