def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print("X", end=" ")
        print()


def solve(board, col, n):

    if col >= n:
        return True

    for row in range(n):
        safe = True

        # Check left side of row
        for i in range(col):
            if board[row][i] == 1:
                safe = False

        # Check upper diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                safe = False
            i -= 1
            j -= 1

        # Check lower diagonal
        i, j = row + 1, col - 1
        while i < n and j >= 0:
            if board[i][j] == 1:
                safe = False
            i += 1
            j -= 1

        if safe:
            board[row][col] = 1

            if solve(board, col + 1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter N: "))

board = [[0] * n for _ in range(n)]

# Place first queen
# board[0][0] = 1

if solve(board, 0, n):
    print("\nFinal N-Queens Matrix:")
    print_board(board, n)
else:
    print("Solution does not exist")