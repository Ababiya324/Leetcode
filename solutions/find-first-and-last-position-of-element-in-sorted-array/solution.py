class Solution(object):
    def searchRange(self, nums, num):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start=0
        end=len(nums)-1
        while start<=end:
            if nums[start]!=num:
                start+=1
            elif nums[end]!=num:
                end-=1
            else:
                return [start,end]
        return [-1,-1]
            
        