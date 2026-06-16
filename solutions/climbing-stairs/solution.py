class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=2
        b=0
        c=1
        for i in range(n):
            c,b=b+c,c
        return c

