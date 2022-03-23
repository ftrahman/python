#
# ps8pr3.py  (Problem Set 8, Problem 3)
#
# Matrix Operations  
#
# Computer Science 111   
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###

def mult_row(matrix, r, m):
    """ multiplies row r of matrix by multiplier
        inputs: matrix is a rectangular 2-D list of numbers
        and r is the row to be multiplied by m
    """
    for c in range(len(matrix[r])):
            matrix[r][c] *= m

def add_row_into(matrix, source, dest):
    """ adds row source of matrix to row dest
        inputs: matrix is a rectangular 2-D list of numbers
        and source is the row to be added to dest
    """
    for c in range(len(matrix[source])):
            matrix[dest][c] +=  matrix[source][c]

def add_mult_row_into(matrix, m, source, dest):
    """ adds row source multiplied by m of matrix to row dest
        inputs: matrix is a rectangular 2-D list of numbers
        and source is the row multipled by m and added to dest
    """
    for c in range(len(matrix[source])):
            matrix[dest][c] +=  m*matrix[source][c]

def transpose(matrix):
    """ tranposes a matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    height = len(matrix)
    width = len(matrix[0])
    matrix2 = []
    for r in range(width):
        row = [0] * height
        matrix2 += [row]
    for r in range(height):
        for c in range(width):
            matrix2[c][r] = matrix[r][c]

    return matrix2

def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)
        elif choice == 2:
            r = int(input('Enter the modified row: '))
            m = float(input('Enter your multiplier: '))
            mult_row(matrix, r, m)
        elif choice == 3:
            source = int(input('Enter your source row: '))
            dest = int(input('Enter your destination row: '))
            add_row_into(matrix, source, dest)
        elif choice == 4:
            m = float(input('Enter your multiplier: '))
            source = int(input('Enter your source row: '))
            dest = int(input('Enter your destination row: '))
            add_mult_row_into(matrix, m, source, dest)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')
