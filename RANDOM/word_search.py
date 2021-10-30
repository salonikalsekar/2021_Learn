class Solution:
    def isWordPresent(self, letters,  words):
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                node = node.setdefault(ch.upper(), {})
            node['$'] = w

        print(trie)

        def traverse(i, j, letters, parent):
            letter = letters[i][j]
            newCurr = parent[letter]
            ismatched = newCurr.pop('$', False)
            if ismatched:
                output.add(ismatched)
            letters[i][j] = '#'
            for newRC in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newR = newRC[0] + i
                newC = newRC[1] + j

                if newR < 0 or newR >= len(letters) or newC < 0 or newC >= len(letters[0]):
                    continue

                if letters[newR][newC] not in newCurr:
                    continue
                traverse(newR, newC, letters, newCurr)
            letters[i][j] = letter

        output = set()
        res = []
        for i in range(len(letters)):
            for j in range(len(letters[0])):
                if letters[i][j] in trie:
                    traverse(i, j, letters, trie)

        for w in words:
            if w.upper() in output:
                res.append('Yes')
            else:
                res.append('No')
        return res

print(Solution().isWordPresent([], ["abcb"]))

print(Solution().isWordPresent([["a","b"],["c","d"]], ["abcb"]))
print(Solution().isWordPresent([["a","b"],["c","d"]], []))
print(Solution().isWordPresent([['M', 'O', 'M'], ['S', 'O', 'N'], ['R', 'A', 'T']], ['MOM', 'MOM', 'MSR', 'OOB']))