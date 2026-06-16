class Solution(object):
    import math
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        d=31
        c=0
        while n>0:
            c+=n%2*(2**d)
            n//=2
            d-=1
        return c 

        