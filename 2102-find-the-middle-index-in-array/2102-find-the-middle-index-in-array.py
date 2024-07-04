class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        def findSum():
            res = 0
            for i in range(len(nums)):
                res += nums[i]
            return res
        tot = findSum()
        leftSum = 0
        for middleIndex in range(len(nums)):
            rightSum = tot - leftSum - nums[middleIndex]
            if leftSum == rightSum:
                return middleIndex
            leftSum += nums[middleIndex]
        return -1