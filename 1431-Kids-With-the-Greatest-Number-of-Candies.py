class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # Initialize max_candies
        max_candies = max(candies)
        # Initialize result list
        result = []
        for i in range(len(candies)):
            # Check if the current child can have the most candies
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
