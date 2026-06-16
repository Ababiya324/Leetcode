class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        o=set()
        sum=0
        for i in nums:
            if i not in o:
             o.add(i)
             sum+=i
            else:
             sum-=i
        return sum