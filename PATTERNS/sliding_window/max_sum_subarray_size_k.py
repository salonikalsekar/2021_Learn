def maxSumSubarray(k, arr):

    startIdx = 0
    total = 0

    window_total = 0

    for endIdx in range(len(arr)):

        window_total += arr[endIdx]

        if endIdx >= k - 1:
            total = max(total, window_total)
            window_total -= arr[startIdx]
            startIdx += 1

    return total


print(maxSumSubarray(3, [2, 1, 5, 1, 3, 2]))
print(maxSumSubarray(2, [2, 3, 4, 1, 5]))