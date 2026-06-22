class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        d="0123456789"
        a=0
        b=0
        for i in num1:
            a=a*10+d.index(i)
        for j in num2:
            b=b*10+d.index(j)
        return str(a*b)

        