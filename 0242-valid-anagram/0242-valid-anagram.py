class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t = Counter(t)
        s = Counter(s)
        print(t)
        print(s)
        return s==t 