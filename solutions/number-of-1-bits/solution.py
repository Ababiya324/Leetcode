class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        while n>0:
                c+=n%2

                n//=2
        return c
        