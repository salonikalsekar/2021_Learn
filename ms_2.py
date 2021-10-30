# loop through the board
# check the live neighbours
# we will also consider the edge cases - within the board (check length)
# compare the total live neighbours  with the conditions
# update the board - if dead - '$' if alive '$$'
# we will loop through the board - update  - '$' - 0 and'$$' with 1

# [$ 0 0
#  0 1 0
#  0 0 0 ]

class Solution:
    def check_next_state(self, board):

        row_length = len(board) # 3
        col_length = len(board[0]) # 3

        visited = [0 * col_length for i in range(row_length)]

        check_neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for i in range(row_length):
            for j in range(col_length):

                total_live_neighbors = 0

                for coord in check_neighbours:

                    new_i = i + coord[0]
                    new_j = j + coord[1]

                    if new_i >= 0 and new_j >= 0 and new_i < row_length and new_j < col_length:
                        if board[new_i][new_j] == 1:
                            total_live_neighbors += 1


                if board[i][j] == 1 and (total_live_neighbors == 1 or total_live_neighbors == 0 or total_live_neighbors >= 4):
                    visited[i][j] = '$' # dead

                if board[i][j] == 1 and (total_live_neighbors == 2 or total_live_neighbors == 3):
                    visited[i][j] = '$$' # alive

                if board[i][j] == 0 and total_live_neighbors == 3:
                    visited[i][j] = '$$' # alive


        for i in range(row_length):
            for j in range(col_length):
                if visited[i][j] == '$$':
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return board





