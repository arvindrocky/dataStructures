from typing import List


class Solution:
    def __init__(self):
        pass

    def calculate_n_queens(self, number_of_queens: int) -> None:
        board = [None] * number_of_queens
        self.calculate_n_queens_helper(number_of_queens, board, 0)

    def calculate_n_queens_helper(self, number_of_queens: int, board: List, row: int) -> None:
        if row == number_of_queens:
            self.print_board(board)
        for j in range(number_of_queens):
            if not self.is_valid_board(board, row, j):
                current_board = board.copy()
                current_board[row] = j
                self.calculate_n_queens_helper(number_of_queens, current_board, row + 1)

    # noinspection PyMethodMayBeStatic
    def is_valid_board(self, board: List, row, column) -> bool:
        has_conflict = False
        for current_row in range(row):
            delta_row = abs(current_row - row)
            delta_column = abs(board[current_row] - column)
            if delta_row == delta_column or board[current_row] == column:
                has_conflict = True
                break
        return has_conflict

    # noinspection PyMethodMayBeStatic
    def print_board(self, board: List) -> None:
        print("Board is: {}".format(board))


a = Solution()
a.calculate_n_queens(4)
