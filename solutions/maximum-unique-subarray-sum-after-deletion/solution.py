class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=[i for i in nums if i>0]
        return sum(set(num)) if len(set(num))>0 else max(nums)