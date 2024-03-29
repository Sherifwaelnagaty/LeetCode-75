class Solution(object):
    def maxVowels(self, s, k):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = k
        count = 0
        max_count = 0

        for i in range(left, right):
            if s[i] in vowels:
                count += 1
        
        max_count = max(count, max_count)

        while right < len(s):
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            max_count = max(count, max_count)
            left += 1
            right += 1

        return max_count
