class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num=set(nums)
        c=[]
        o=max(num)
        p=min(num)
        for i in range(p,o+1):
            if i not in num:
                c.append(i)
        return c
