class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        curr_word, idx, min_length = None, 0, len(wordsDict)

        for i, w in enumerate(wordsDict):

            if w not in (word1, word2):
                continue
            if curr_word and (word1 == word2 or w != curr_word):
                min_length = min(min_length, i - idx)

            curr_word, idx = w, i

        return min_length