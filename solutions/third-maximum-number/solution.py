class Solution(object):
    def thirdMax(self, nums):
        first = second = third = None

        nums = list(set(nums))   # remove duplicates
        
        if len(nums) < 3:
            return max(nums)
        
        nums.remove(max(nums))
        nums.remove(max(nums))
        
        return max(nums)