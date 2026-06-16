class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        m=0
        n=0
        for i in bills:
            if i==5:
                m+=1
            elif i==10:
                if m==0:
                    return False
                m-=1
                n+=1
            else:
                if n>0 and m>0:
                    n-=1
                    m-=1
                elif m>=3:
                    m-=3
                else:
                 return False
        return True

        