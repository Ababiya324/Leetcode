class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = 0
        e = 0
        for num in nums:
            d = (d + num) * num
            if d > e:
                e = d
        return e

        