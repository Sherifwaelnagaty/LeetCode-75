class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            small = []
            large = []
            equal = []

            pivot_num = random.choice(nums)

            for num in nums:
                if num == pivot_num:
                    equal.append(num)
                elif num < pivot_num:
                    small.append(num)
                else:
                    large.append(num)
            
            if k <= len(large):
                return quick_select(large, k)
            
            if k > len(large) + len(equal):
                return quick_select(small, k - len(large) - len(equal))
            
            return pivot_num
        return quick_select(nums, k)