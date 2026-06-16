class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x==0 or x<-2**31 or x>(2**31)-1):
            return 0
        c = -1 if x < 0 else 1
        x=abs(x)
        i=0
        v=0
        while(x>0):
            v=v*10+(x%10)
            x//=10
            i+=1
        if v < -2**31 or v > (2**31) - 1:
            return 0
        return c*v

