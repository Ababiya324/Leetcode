class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num=set(nums)
        for i in range(k,max(num)+2*k,k):
            
                if i not in num:
                 return i
                
        