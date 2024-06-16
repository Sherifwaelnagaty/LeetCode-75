class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maximum = 0
        for p in range(n):
            unique_chars = set()
            for p1 in range(p, n):
                if s[p1] not in unique_chars:
                    unique_chars.add(s[p1])
                    maximum = max(maximum, len(unique_chars))
                else:
                    break
        return maximum