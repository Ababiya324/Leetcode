class Solution(object):
    def scoreBalance(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=[]
      
        for i in range(len(s)):
            c.append(ord(s[i])-96)
        a=sum(c)
        for i in range(1,len(c)):
            d=sum(c[:i])
            if d==a-d:
                return True
            if d>a-d:
                 return False  
        return False



        