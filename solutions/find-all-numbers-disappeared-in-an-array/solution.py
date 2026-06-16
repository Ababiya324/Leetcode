class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=set(nums)
        k=[]
        for i in range(1,len(nums)+1):
            if i not in d:
                k.append(i)
        return k


        