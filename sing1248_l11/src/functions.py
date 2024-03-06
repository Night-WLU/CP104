"""
-------------------------------------------------------
[Functions for Lab 11]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
import random


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    for _ in range(rows):
        row = []  # define a new row
        for _ in range(cols):
            if value_type == 'float':
                value = random.uniform(low, high)
            elif value_type == 'int':
                value = random.randint(low, high)
            row.append(value)  # add value to row
        matrix.append(row)  # add new row to matrix
    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    counter_2 = 0
    cols = ""
    rows = ""
    for i in range(0, len(matrix), 1):
        if i > 0:
            rows += "\n"
        rows += f"{counter_2:<3d}"
        for j in range(len(matrix[i])):
            if value_type == 'float':
                rows += f"{(matrix[i][j]):>5.2f}    "
            elif value_type == 'int':
                rows += f"{(matrix[i][j]):>5d}"
        counter_2 += 1
    if value_type == 'float':
        for i in range(len(matrix[0])):
            if i == 0:
                cols += f"{i:>8d}"
            else:
                cols += f"{i:>9d}"
    elif value_type == 'int':
        for i in range(len(matrix[0])):
            if i == 0:
                cols += f"{i:>8d}"
            else:
                cols += f"{i:>5d}"
    print(cols)
    print(rows)
    return None


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    s_loc_temp = matrix[0][0]
    l_loc_temp = matrix[0][0]
    for i in range(0, len(matrix), 1):
        for j in range(len(matrix[i])):
            if (matrix[i][j]) <= s_loc_temp:
                s_loc = []
                s_loc.append(i)
                s_loc.append(j)
            if (matrix[i][j]) >= l_loc_temp:
                l_loc = []
                l_loc.append(i)
                if j > 0:
                    l_loc.append(j-1)
                else:
                    l_loc.append(j)
    return s_loc, l_loc


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] * num
    return None


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    transposed = []
    for i in range(len(matrix[0])):
        row = []  # define a new row
        for j in range(len(matrix)):
            value = matrix[j][i]
            row.append(value)  # add value to row
        transposed.append(row)  # add new row to matrix
    return transposed
