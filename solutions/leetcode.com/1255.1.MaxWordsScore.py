class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        if not words:
            return 0
        counts = collections.Counter(letters)
        word = words.pop(0)
        possible = True
        result = 0
        for char in word:
            if char not in counts or counts[char] == 0:
                possible = False
                break
            else:
                counts[char] -= 1
                result += score[ord(char) - ord('a')]
        if not possible:
            result = self.maxScoreWords(words.copy(), letters, score)
        else:
            newLetters = []
            for key in counts:
                newLetters += [key]*counts[key]
            result = max(result + self.maxScoreWords(words.copy(), newLetters, score), self.maxScoreWords(words.copy(), letters, score))
        return result
    
# metadata
# relevant-topics recursion
# time-complexity O(2^N) 30.39%
# space-complexity O(N) 53.06%
# language python
# difficulty hard
# date 20240524