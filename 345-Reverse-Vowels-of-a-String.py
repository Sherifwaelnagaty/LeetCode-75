class Solution:
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_in_string = [char for char in s if char in vowels]
        reversed_vowels = vowels_in_string[::-1]

        result = ''
        vowel_index = 0
        for char in s:
            if char in vowels:
                result += reversed_vowels[vowel_index]
                vowel_index += 1
            else:
                result += char
        
        return result



        