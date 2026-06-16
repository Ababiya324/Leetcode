class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        d = 0
        for i in count: 
            if i+1 in count:
                d = max(d, count[i] + count[i+1])

        return d
        