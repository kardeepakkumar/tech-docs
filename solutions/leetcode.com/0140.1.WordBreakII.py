class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        for i in range(0, len(s)):
            if s[0:i+1] in wordDict:
                if i != len(s) - 1:
                    subResult = self.wordBreak(s[i+1:], wordDict)
                    for r in subResult:
                        result += [s[0:i+1] + " " + r]
                else:
                    result += [s[0:i+1]]
        return result

# metadata
# relevant-topics recursion
# time-complexity O(N * 2^N) 47.42%
# space-complexity O(N) 87.62%
# language python
# difficulty hard
# date 20240525