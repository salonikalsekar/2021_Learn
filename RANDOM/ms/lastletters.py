def anagram_difference(a, b):
    res = []
    for i in range(len(a)):
        str_a = a[i]
        str_b = b[i]
        if len(str_a) != len(str_b):
            res.append(-1)
        else:
            a_list = [0] * 26
            b_list = [0] * 26
            diffs = 0
            for j in range(len(str_a)):
                a_list[ord(str_a[j]) - 97] += 1
                b_list[ord(str_b[j]) - 97] += 1
            for k in range(0, len(a_list)):
                if a_list[k] != b_list[k]:
                    diffs += abs(a_list[k] - b_list[k])
            res.append(int(diffs/2))
    return res


print(anagram_difference(['to', 'tea', 'act'], ['at', 'teas', 'atcs']))