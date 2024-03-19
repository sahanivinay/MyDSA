def zeroMatrix(matrix, n, m):
    col = [0] * m
    row = [0] * n

    # Mark rows and columns containing 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    # Zero out rows and columns based on the marks
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0

    return matrix

# Example usage
matrix = [
    [2, 4, 3],
    [1, 0, 0]
]

n = 2
m = 3

result = zeroMatrix(matrix, n, m)
for row in result:
    print(" ".join(map(str, row)))
