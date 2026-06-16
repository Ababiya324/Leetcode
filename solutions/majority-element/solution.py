class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for x in nums:
            if count == 0:
                candidate = x
            if x == candidate: 
             count += 1
            else:
                 count-=1

        return candidate



        