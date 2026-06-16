class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=sorted(nums)
        return a[-1]+a[-2]-a[0]