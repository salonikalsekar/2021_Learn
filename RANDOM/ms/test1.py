def moves(arr):
    left = 0
    right = len(arr) - 1
    c = 0
    while left < right:
        if arr[left] % 2 == 0:
            left += 1
            continue

        if arr[right] % 2 != 0:
            right -= 1
            continue

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        c += 1
    
    return c


print(moves([5, 7, 3, 1, 2, 4]))
print(moves([1,2,4,5]))
