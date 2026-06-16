class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        a=[]
        d=0
        m=sum(nums)//2
        for i in nums:
            a.append(i)
            d+=i
            if d>m:
                return a
            
