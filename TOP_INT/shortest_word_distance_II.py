from collections import Counter


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.locations = defaultdict(list)

        for i, w in enumerate(wordsDict):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = 0, 0
        min_length = float('inf')

        loc1, loc2 = self.locations[word1], self.locations[word2]

        while l1 < len(loc1) and l2 < len(loc2):
            min_length = min(min_length, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1

        return min_length