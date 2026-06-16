class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=1
        d=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                s+=1
            else:
                d=max(s,d)
                s=1
        
        return max(s,d)

        