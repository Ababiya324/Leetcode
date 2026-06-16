class Solution(object):
    def largestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c=-1*float('inf')
        d=0
        for i in range(len(nums)-k+1):
           if  nums[i]>c:
            c=nums[i]
            d=i
        return nums[d:d+k]