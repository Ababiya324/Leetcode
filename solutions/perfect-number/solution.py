class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a = [6,28,496,8128,33550336]
        return True if num in a else False
        if num==1:
            return False
        c=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                c+=i
                if i!=num//i:
                    c+=num//i
                    
        return c==num
            

        