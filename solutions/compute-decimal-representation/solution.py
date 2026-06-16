class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i=0
        c=[]
        while n>0:
          if n%10!=0:
            c.append((n%10)*10**i)
          n//=10
          i+=1
        return c[::-1]
        
        