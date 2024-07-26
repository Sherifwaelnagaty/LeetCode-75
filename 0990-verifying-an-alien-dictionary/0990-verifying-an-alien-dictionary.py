class Solution:
    def isAlienSorted(self, words, order):
        order_map = {char: idx for idx, char in enumerate(order)}
        
        def is_ordered(word1, word2):
            for c1, c2 in zip(word1, word2):
                if order_map[c1] < order_map[c2]:
                    return True
                elif order_map[c1] > order_map[c2]:
                    return False
            return len(word1) <= len(word2)
        
        return all(is_ordered(words[i], words[i + 1]) for i in range(len(words) - 1))

        