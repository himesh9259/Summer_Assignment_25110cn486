# Check Symmetric Matrix

matrix = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]

symmetric = True

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

if symmetric:
    print("Matrix is Symmetric")
else:
    print("Matrix is Not Symmetric")
