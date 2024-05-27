class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)+1
        result = ""
        l, r = 0, 0
        counts = Counter(t)
        while r < len(s):
            if s[r] in counts.keys():
                counts[s[r]] -= 1
                if counts.most_common(1)[0][1] == 0:
                    while s[l] not in counts.keys() or counts[s[l]] < 0:
                        if s[l] in counts.keys():
                            counts[s[l]] += 1
                        l += 1
                    if length > r-l+1:
                        length = r-l+1
                        result = s[l:r+1]
                        if length == len(t):
                            break
                    stopNext = False
                    while l <= r:
                        if s[l] in counts.keys():
                            counts[s[l]] += 1
                            if not stopNext and counts[s[l]] > 0:
                                stopNext = True
                            elif stopNext and counts[s[l]] > 0:
                                counts[s[l]] -= 1
                                break
                        l += 1
            r += 1
        return result

# metadata
# relevant-topics Sliding window
# time-complexity O(N) 15.21%
# space-complexity O(N) 39.06%
# language python
# difficulty hard
# date 20240527