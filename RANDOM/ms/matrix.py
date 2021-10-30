def findBeforeMatrix(after):
    lengthRow = len(after)
    lengthColumn = len(after[0])

    before = [[0 for _ in range(lengthColumn)] for _ in range(lengthRow)]

    if lengthRow == 0:
        return []

    if lengthColumn == 0:
        return []

    for i in range(0, lengthRow):
        acc = 0
        for j in range(0, lengthColumn):
            if i - 1 < 0:
                up_sum = 0
            else:
                after[i-1][j]

            left_sum = 0 if j - 1 < 0 else acc
            cur = after[i][j] - up_sum - left_sum
            before[i][j] = cur
            acc += cur
    return before

rst = findBeforeMatrix([[2, 1], [5, 4]])
print(rst)
rst = findBeforeMatrix([[1,2,3], [3,4,5], [6, 7, 8]])
print(rst)