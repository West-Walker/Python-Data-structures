def sum_up_diagonals(matrix):
    diagonal_sum = 0
    rows = len(matrix)
    
    for i in range(rows):
        diagonal_sum += matrix[i][i]  # Add elements from main diagonal
        diagonal_sum += matrix[i][rows-i-1]  # Add elements from secondary diagonal
    
    return diagonal_sum