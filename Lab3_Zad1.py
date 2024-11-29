# Stanisław Kusiak

def matrix_mult(x, y):
    for i in range(1, len(x)):
        if len(x[0]) != len(x[i]):
            return -1
    for i in range(1, len(y)):
        if len(y[0]) != len(y[i]):
            return -1

    if len(x[0]) != len(y):
        return -1
    else:
        result = [[0 for x in range(len(x))] for y in range(len(y[0]))]
        # Rows of lhs matrix
        for i in range(len(x)):
            # Columns of rhs matrix
            for j in range(len(y[0])):
                # Columns of lhs matrix and rows of rhs matrix
                for k in range(len(y)):
                    result[i][j] += x[i][k] * y[k][j]
        return result


m1 = [[1, 2, 3],
      [1, 1, 1],
      [3, 2, 1]]

m2 = [[3, 2, 1],
      [1, 1, 1],
      [1, 2, 3]]

print(matrix_mult(m1, m2))

