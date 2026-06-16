class Solution(object):
    def smallestAbsent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q=1+sum(nums)//len(nums)
        if q<=0:
            q=1
        while q in set(nums):
            q+=1
        return q