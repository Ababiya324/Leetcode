class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a={}
        c=0
        for i in nums:
            a[i]=a.get(i,0)+1
        for i in a:
            if a[i]%k==0:
                c+=a[i]*i
        return c
