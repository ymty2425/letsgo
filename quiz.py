def reverse_list(l:list):

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

    TODO: Write a programme to solve 9x9 Sudoku board.

 

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

 

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """

    pass

def main():
    # Test reverse_list function
    test_list = [1, 2, 2, 3, 4, 4, 12]
    print("Original list:", test_list)
    
    reversed_list = reverse_list(test_list)
    print("Reversed list:", reversed_list)  # Output should be [12, 4, 4, 3, 2, 2, 1]

if __name__ == "__main__":
    main()