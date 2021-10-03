def rotate(row, col, matrix) -> None:
    matrix.reverse()

    for i in range(row):
        for j in range(i + 1, col):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix

print(rotate(3 , 3 , [[1,2,3], [4,5,6], [7,8,9]]))