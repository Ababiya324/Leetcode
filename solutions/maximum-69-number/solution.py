class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        i=0
        j=-1
        c=num
        while num>0:
            x=num%10
            if x==6:
                j=i
            i+=1
            num//=10
        if j>=0:
         c+=3*10**j
        return c
        