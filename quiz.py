def reverse_list(l: list):
    """

    Reverse a list without using any built-in functions.

    The function takes a list as input and returns a new list
    that is the reverse of the input list.

    Parameters:
    l (list): The input list which can contain any type of data.

    Returns:
    list: The reversed list.

    """

    start = 0
    end = len(l) - 1

    while start < end:
        # Swap the elements at the start and end indices
        l[start], l[end] = l[end], l[start]
        # Move towards the middle
        start += 1
        end -= 1

    return l


def solve_sudoku(matrix):
    """

    Solve a 9x9 Sudoku board using the backtracking algorithm.

    The function modifies the input 9x9 matrix in-place to solve the Sudoku puzzle.
    It ensures that each row, column, and 3x3 subgrid contains all of the digits
    from 1 to 9 without repetition.

    Parameters:
    matrix (list of list of int): A 9x9 matrix representing the Sudoku board.
                                  Empty cells are represented by 0.

    Returns:
    list of list of int: The solved Sudoku board.

    """

    def valid_move(row, col, num):
        """

        Check if placing a number at a specific position is valid according to Sudoku rules.

        Parameters:
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        num (int): The number to place in the cell.

        Returns:
        bool: True if the move is valid, False otherwise.

        """

        # Check if the number is not present in the current row
        for i in range(9):
            if matrix[i][col] == num:
                return False
            if matrix[row][i] == num:
                return False
            # Check if the number is not present in the current 3x3 subgrid
            if matrix[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def backtrack():
        """

        Backtracking function to solve the Sudoku board by trying all possible numbers
        in empty cells and recursively solving the resulting board.

        Returns:
        bool: True if the board is solved, False otherwise.

        """

        for i in range(9):
            for j in range(9):
                # Find the empty cell
                if matrix[i][j] == 0:
                    for num in range(1, 10):
                        if valid_move(i, j, num):
                            matrix[i][j] = num
                            if backtrack():
                                return True
                            # If the current move is not valid, backtrack
                            matrix[i][j] = 0
                    return False
        return True

    if backtrack():
        return matrix
    else:
        return None


def main():
    # Test reverse_list function
    test_list = [1, 2, 2, 3, 4, 4, 12]
    print("Original list:", test_list)

    reversed_list = reverse_list(test_list)
    print("Reversed list:", reversed_list)  # Output should be [12, 4, 4, 3, 2, 2, 1]

    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 1, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("\nOriginal Sudoku board:")
    for row in sudoku_board:
        print(row)

    solved_sudoku = solve_sudoku(sudoku_board)

    if solved_sudoku:
        print("\nSolved Sudoku board:")
        for row in solved_sudoku:
            print(row)
    else:
        print("Invalid Sudoku")


if __name__ == "__main__":
    main()
