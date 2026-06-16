class Solution(object):
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                # left is odd, right is even - swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] % 2 == 0:
                # left is even, already correct - move forward
                left += 1
            else:
                # right is odd, already correct - move backward
                right -= 1
        
        return nums