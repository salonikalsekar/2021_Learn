def closestNumbers(arr):
    arr.sort()

    diffVal = []
    for index in range(len(arr) - 1):
        diffVal.append(abs(arr[index] - arr[index + 1]))
  
    result = []
    minimum_diff = min(diffVal)

    for index, num in enumerate(diffVal):
        if num == minimum_diff:
            result.append([arr[index], arr[index + 1]])

    return result

print(closestNumbers([6,2,4,10]))
print(closestNumbers([4,2,1,3]))
print(closestNumbers([4,-2,-1,3]))