class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen=set()
        for i in range(len(nums)):
            if target-nums[i] in seen:
                return (i,nums.index(target-nums[i])) 
            else:
                seen.add(nums[i])
