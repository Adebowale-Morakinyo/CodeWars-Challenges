def get_matrix_product(a, b):
    # Check if matrices can be multiplied
    if len(a[0]) != len(b):
        return None
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    
    # Perform matrix multiplication
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    
    return result
