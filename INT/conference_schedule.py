def confSchedule(n, startArr, endArr):
    sl = sorted((list(zip(*[startArr, endArr]))), key=lambda x: x[1])
    sl = list(zip(*sl))
    lim = sl[1][0]
    total = 1
    for i in range(1, n):
        if sl[0][i] >= lim:
            total += 1
            lim = sl[1][i]
    return total


print(confSchedule(3, [1,1,2], [3,2,4]))
print(confSchedule(4, [1,1,2, 3], [2,3,3,4]))
print(confSchedule(4, [6,1,2, 3], [8,9,4,7]))