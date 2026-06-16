class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        d=0
        i=1
        while n>0:
            if n%10!=0:
             c+=n%10*i
             d+=n%10
             i*=10
            n=n//10
        return c*d
        