class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = set(range(1,len(nums)+1))
        b=set(nums)
        c=sum(a-b)
        d=sum(nums)-sum(b)
        return [d,c]
        