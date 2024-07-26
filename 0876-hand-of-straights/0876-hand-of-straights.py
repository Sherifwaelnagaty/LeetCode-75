class Solution:
    def isNStraightHand(self,hand, W):
        if len(hand) % W != 0:
            return False
        
        count = Counter(hand)
        hand.sort()
        
        for card in hand:
            if count[card] > 0:
                for i in range(card, card + W):
                    if count[i] > 0:
                        count[i] -= 1
                    else:
                        return False
        return True
