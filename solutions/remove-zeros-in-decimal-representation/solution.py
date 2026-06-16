class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        i=0
        while n>0:
            if n%10!=0:
                c+=(n%10*10**i)
                i+=1
            n//=10
        return c
